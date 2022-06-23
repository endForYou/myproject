from appium import webdriver
import db
from src.base import Base
from mylib import *


class HnMajorScoreLine(Base):

    def execute_all(self):
        driver = self.driver
        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_logo")
        find_college_element.click()
        # 点击筛选层次
        find_all_college_element = driver.find_elements(by=AppiumBy.ID,
                                                        value="com.eagersoft.youzy.youzy:id/tab_layout_text")[1]
        find_all_college_element.click()
        # 本科
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/recycler_level").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[0].click()
        # 点击确定
        driver.find_element(by=AppiumBy.ID,
                            value="com.eagersoft.youzy.youzy:id/sgb_confirm").click()
        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        colleges = get_all_colleges(cursor, province="湖南", data_type="major_score_line")
        no_need_colleges = get_all_colleges_of_no_need(cursor, province="湖南", data_type="major_score_line")
        for i in range(0, 500):
            self.get_one_page_major_score_line_of_ben(colleges, no_need_colleges)
            self.next_page()

        self.driver.quit()

    def get_one_page_major_score_line_of_ben(self, colleges, no_need_colleges):
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        province = "湖南"
        driver = self.driver
        data_type = "major_score_line"
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_cl_parent")))
        # print(driver.page_source)
        for i in range(0, college_list_element_count):
            college_element = \
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_cl_parent")[i]
            if not is_element_present_by_element(college_element, "com.eagersoft.youzy.youzy:id/tv_name"):
                college_element.click()
            else:
                college_name = college_element.find_element(by=AppiumBy.ID,
                                                            value="com.eagersoft.youzy.youzy:id/tv_name").text
                # 如果college_name 在不需要的colleges 或者在已经爬取的college 或者在self的college_list就不需要爬取了
                if college_name in no_need_colleges or college_name in colleges or college_name in self.college_list:
                    continue

                college_element.click()

            title_college_name = driver.find_element(by=AppiumBy.ID,
                                                     value="com.eagersoft.youzy.youzy:id/tv_college_name").text
            if title_college_name in no_need_colleges or title_college_name in colleges or title_college_name in self.college_list:
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_back")
                back_element.click()
            else:
                el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
                el15.click()
                # 点击专业分数线tab
                # 把college_name 写进数据库
                self.college_list.append(title_college_name)
                insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=None)
                driver.tap([(540, 238), ])
                time.sleep(1)
                if not is_element_present(self.driver,
                                          "com.eagersoft.youzy.youzy:id/material_spinner_year"):
                    # 如果这里没加载出来，直接返回
                    # 点击从专业分数线回退
                    # 把college_name 写进数据库
                    insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=1)
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                    back_element.click()
                    # 点击从院校详情回退回退
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_back")
                    back_element.click()
                    continue
                course_text = driver.find_element(by=AppiumBy.ID,
                                                  value="com.eagersoft.youzy.youzy:id/material_spinner2_course").text.strip()
                if course_text == "物理":
                    # 默认
                    grade = "本科"
                    science_art = "物理"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        0].click()
                    grade = "本科"
                    science_art = "历史"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        0].click()
                else:
                    # 默认
                    grade = "本科"
                    science_art = "历史"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        0].click()
                    grade = "本科"
                    science_art = "物理"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        1].click()
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_back")
                back_element.click()


if __name__ == "__main__":
    # db = DataBase().get_cursor()
    caps = {"platformName": "Android", "appium:platformVersion": "10", "appium:deviceName": "MI_CC_9",
            "appium:appPackage": "com.eagersoft.youzy.youzy", "appium:appActivity": ".mvvm.ui.launch.LaunchActivity",
            "appium:ensureWebviewsHavePages": True, "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True, 'noReset': True, 'fullReset': False,
            'settings[waitForIdleTimeout]': 10,
            "automationName": "UiAutomator2"}
    my_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    my_driver.implicitly_wait(10)
    obj = HnMajorScoreLine(my_driver)
    obj.execute_all()
