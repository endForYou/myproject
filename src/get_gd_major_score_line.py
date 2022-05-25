from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db


class MajorScoreLine:
    def __init__(self, driver):
        self.driver = driver
        self.college_list = []

    def execute_all(self):
        driver = self.driver

        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        colleges = get_all_colleges_yn(cursor, province="广东")
        for i in range(0, 190):
            self.next_page()

        for i in range(0, 500):
            self.get_one_page_major_score_line(colleges)
            self.next_page()

        self.driver.quit()

    # def is_repeat_page(self):
    #     college_elements = self.driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name")
    #     for college in college_elements:
    #         college_name = college.text
    #         if college_name not in self.college_list:
    #             return False
    #     return True

    def next_page(self):
        driver = self.driver
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(439, 1200)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(439, 414)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)

    def is_repeat_detail_page(self, major_name_list):
        if not is_element_exist(self.driver, "com.eagersoft.youzy.youzy:id/recycler_view"):
            return True
        major_elements = self.driver.find_element(by=AppiumBy.ID,
                                                  value="com.eagersoft.youzy.youzy:id/recycler_view").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_major_name")
        for major in major_elements:

            major_name = major.text

            if major_name not in major_name_list:
                return False
        return True

    def execute_one_tab_major_score_line(self):
        driver = self.driver
        if is_element_exist(driver, element="com.eagersoft.youzy.youzy:id/cl_college"):

            enroll_direction_list_count = len(
                list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")))
            for i in range(0, enroll_direction_list_count):
                driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
                enroll_direction = \
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")[i]
                # 点击某个招生方向
                enroll_direction.click()
                # 最后需要关闭招生方向的toast
                driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_close").click()

    def get_one_page_major_score_line(self, colleges):
        driver = self.driver
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
                if college_name in colleges:
                    continue
                if college_name not in self.college_list:
                    self.college_list.append(college_name)
                else:
                    continue
                college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
            el15.click()
            # 点击专业分数线tab

            title_college_name = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/title").text
            if title_college_name in colleges:
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()
            else:
                driver.tap([(540, 238), ])
                # 点击招生方向,先判断有没有招生方向
                # 默认
                grade = "本科"
                science_art = "历史"

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
    obj = MajorScoreLine(my_driver)
    obj.execute_all()
