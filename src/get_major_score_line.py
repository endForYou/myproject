from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *


class MajorScoreLine:
    def __init__(self, driver):
        self.driver = driver
        self.college_list = []

    def execute_all(self):
        driver = self.driver
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        time.sleep(3)
        while True:
            # if self.is_repeat_page():
            #     break
            self.get_one_page_major_score_line()
            # print(111111)
            self.next_page()
            break
        self.driver.quit()

    def is_repeat_page(self):
        college_elements = self.driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name")
        for college in college_elements:
            college_name = college.text
            if college_name not in self.college_list:
                return False
        return True

    def next_page(self):
        time.sleep(1)
        driver = self.driver
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(439, 1480)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(439, 414)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)

    def get_one_tab_major_score_line(self):
        driver = self.driver
        time.sleep(1)
        if is_element_exist(driver, element="com.eagersoft.youzy.youzy:id/cl_college"):
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
            enroll_direction_list_count = len(
                list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")))
            for i in range(0, enroll_direction_list_count):
                enroll_direction = \
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")[i]
                # 点击某个招生方向
                print(driver.page_source)
                enroll_direction.click()
                # 专业分数线列表
                major_list = []
                major_score_line_list_element = driver.find_element(by=AppiumBy.ID,
                                                                    value="com.eagersoft.youzy.youzy:id/recycler_view")
                for major_score_line_element in major_score_line_list_element.find_elements(by=AppiumBy.ID,
                                                                                            value="com.eagersoft.youzy.youzy:id"
                                                                                                  "/parent"):
                    pass
                    # major_name = major_score_line_element.find_element(by=AppiumBy.ID,
                    #                                                    value="com.eagersoft.youzy.youzy:id/tv_major_name").text
                    # if major_name not in major_list:
                    #     major_list.append(major_name)
                    # else:
                    #     continue
                    # subject_need = major_score_line_element.find_element(by=AppiumBy.ID,
                    #                                                      value="com.eagersoft.youzy.youzy:id/tv_choose").text
                    # enroll_count = major_score_line_element.find_element(by=AppiumBy.ID,
                    #                                                      value="com.eagersoft.youzy.youzy:id/tv_enrollment").text
                    # highest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                    #                                                       value="com.eagersoft.youzy.youzy:id/tv_score").text
                    # lowest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                    #                                                      value="com.eagersoft.youzy.youzy:id/tv_seating").text
                # 循环的最后需要再次点击招生方向切换
                driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
                # 点击close
            # 最后需要关闭招生方向的toast
            time.sleep(1)
            if is_element_exist(driver, "com.eagersoft.youzy.youzy:id/iv_close"):
                driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_close").click()

    def get_one_page_major_score_line(self):
        driver = self.driver
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")))
        print(driver.page_source)
        for i in range(0, college_list_element_count):
            if i >= 8:
                continue

            college_element = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")[i]
            college_name = college_element.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name")
            if college_name not in self.college_list:
                self.college_list.append(college_name)
            else:
                continue
            college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
            el15.click()
            # 点击专业分数线tab
            driver.tap([(540, 238), ])

            # 点击招生方向,先判断有没有招生方向
            self.get_one_tab_major_score_line()
            # 点击本科专科
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
            # 点击专科（默认本科）
            driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                1].click()
            self.get_one_tab_major_score_line()
            # 点击历史（默认物理）
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
            driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                1].click()
            self.get_one_tab_major_score_line()
            # 点击本科专科
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
            # 点击本科
            driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                0].click()
            # 点击招生方向
            self.get_one_tab_major_score_line()
            # 点击从专业分数线回退
            back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
            back_element.click()
            # 点击从院校详情回退回退
            back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
            back_element.click()


if __name__ == "__main__":
    # db = DataBase().get_cursor()
    caps = {"platformName": "Android", "appium:platformVersion": "11", "appium:deviceName": "Lenovo_L79031",
            "appium:appPackage": "com.eagersoft.youzy.youzy", "appium:appActivity": ".mvvm.ui.launch.LaunchActivity",
            "appium:ensureWebviewsHavePages": True, "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True, 'noReset': True, 'fullReset': False,
            'settings[waitForIdleTimeout]': 10}
    my_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    my_driver.implicitly_wait(10)
    obj = MajorScoreLine(my_driver)
    obj.execute_all()
