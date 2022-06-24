from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db
from src.base import Base


class GdEnrollStudentPlanLine(Base):

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
        colleges = get_all_colleges(cursor, province="广东", data_type="enroll_plan")
        no_need_colleges = get_all_colleges_of_no_need(cursor, province="广东", data_type="enroll_plan")

        for i in range(0, 400):
            self.get_one_page_enroll_student_plan(colleges, no_need_colleges)
            self.next_page()

        self.driver.quit()

    def get_one_page_enroll_student_plan(self, colleges, no_need_colleges):
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        province = "广东"
        driver = self.driver
        data_type = "enroll_plan"
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
                el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_enter_plan")
                el15.click()
                # 点击专业分数线tab
                # 把college_name 写进数据库
                self.college_list.append(title_college_name)
                insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=None)
                time.sleep(1)
                course_text = driver.find_element(by=AppiumBy.ID,
                                                  value="com.eagersoft.youzy.youzy:id/material_spinner2_course").text.strip()
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
    obj = GdEnrollStudentPlanLine(my_driver)
    obj.execute_all()
