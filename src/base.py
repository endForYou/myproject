from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.college_list = []

    def next_page(self):
        driver = self.driver
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(439, 1400)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(439, 500)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)

    def enter_into_main_page_(self):
        driver = self.driver
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        time.sleep(2)

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
