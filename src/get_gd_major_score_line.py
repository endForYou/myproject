from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db
from src.base import Base
from mylib import *


class HnMajorScoreLine(Base):

    def execute_all(self):
        driver = self.driver
        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_logo")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        # 点击筛选本科
        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        colleges = get_all_colleges(cursor, province="广东", data_type="major_score_line")
        no_need_colleges = get_all_colleges_of_no_need(cursor, province="广东", data_type="major_score_line")
        for i in range(0, 500):
            self.get_one_page_major_score_line(colleges, no_need_colleges)
            self.next_page()

        self.driver.quit()

    def execute_ben(self):
        driver = self.driver

        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_logo")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        # 本科
        choose_element=driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_filter").click()
        batch_element =driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/batch").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[1].click()
        confirm_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_confirm").click()

        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        colleges = get_all_colleges(cursor, province="广东", data_type="major_score_line")
        no_need_colleges = get_all_colleges_of_no_need(cursor, province="广东", data_type="major_score_line")
        for i in range(0, 500):
            self.get_one_page_major_score_line(colleges, no_need_colleges)
            self.next_page()

        self.driver.quit()

    def get_one_page_major_score_line_of_ben(self, colleges, no_need_colleges):
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        driver = self.driver
        province = "广东"
        data_type = "major_score_line"
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")))
        # print(driver.page_source)
        for i in range(0, college_list_element_count):
            college_element = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")[i]
            if not is_element_present_by_element(college_element, "com.eagersoft.youzy.youzy:id/name"):
                college_element.click()
            else:
                college = college_element.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name").text
                college_name = college.split(" ")[0]
                # 如果college_name 在不需要的colleges 或者在已经爬取的college 或者在self的college_list就不需要爬取了
                if college_name in no_need_colleges or college_name in colleges or college_name in self.college_list:
                    continue

                college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
            el15.click()
            # 点击专业分数线tab

            title_college_name = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/title").text
            if title_college_name in no_need_colleges or title_college_name in colleges or title_college_name in self.college_list:
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()
            else:
                # 把college_name 写进数据库
                self.college_list.append(title_college_name)
                driver.tap([(540, 238), ])
                # 点击招生方向,先判断有没有招生方向
                # 默认
                grade = "本科"
                science_art = "历史"
                time.sleep(2)
                if not is_element_present(self.driver,
                                          "com.eagersoft.youzy.youzy:id/material_spinner_year"):
                    # 如果这里没加载出来，直接返回
                    # 点击从专业分数线回退
                    # 把college_name 写进数据库
                    insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=1)
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                    back_element.click()
                    # 点击从院校详情回退回退
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                    back_element.click()
                    continue
                insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=None)

                grade = "本科"
                science_art = "物理"
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    0].click()

                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()

    def get_one_page_major_score_line(self, colleges, no_need_colleges):
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        driver = self.driver
        province = "广东"
        data_type = "major_score_line"
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")))
        # print(driver.page_source)
        for i in range(0, college_list_element_count):
            college_element = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")[i]
            if not is_element_present_by_element(college_element, "com.eagersoft.youzy.youzy:id/name"):
                college_element.click()
            else:
                college = college_element.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name").text
                college_name = college.split(" ")[0]
                # 如果college_name 在不需要的colleges 或者在已经爬取的college 或者在self的college_list就不需要爬取了
                if college_name in no_need_colleges or college_name in colleges or college_name in self.college_list:
                    continue

                college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
            el15.click()
            # 点击专业分数线tab

            title_college_name = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/title").text
            if title_college_name in no_need_colleges or title_college_name in colleges or title_college_name in self.college_list:
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()
            else:
                # 把college_name 写进数据库
                self.college_list.append(title_college_name)
                driver.tap([(540, 238), ])
                # 点击招生方向,先判断有没有招生方向
                # 默认
                grade = "本科"
                science_art = "历史"
                time.sleep(2)
                if not is_element_present(self.driver,
                                          "com.eagersoft.youzy.youzy:id/material_spinner_year"):
                    # 如果这里没加载出来，直接返回
                    # 点击从专业分数线回退
                    # 把college_name 写进数据库
                    insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=1)
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                    back_element.click()
                    # 点击从院校详情回退回退
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                    back_element.click()
                    continue
                insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=None)
                # 点击本科专科
                grade = "专科"
                science_art = "历史"
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    1].click()

                grade = "专科"
                science_art = "物理"
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    1].click()

                grade = "本科"
                science_art = "物理"
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    0].click()

                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
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
    obj.execute_ben()
