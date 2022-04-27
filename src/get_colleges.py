from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db


class Colleges:
    def __init__(self, driver):
        self.driver = driver
        self.college_list = []

    def execute_all(self):
        """
        如果一次性没跑完，可能需要跑的时候先翻页
        :return:
        """
        driver = self.driver
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        time.sleep(3)
        # my_db = db.DataBase()
        # cursor = my_db.get_cursor()
        for i in range(0, 500):
            self.next_page()

        self.driver.quit()

    def next_page(self):
        driver = self.driver
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(439, 1480)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(439, 414)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(1)


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
    obj = Colleges(my_driver)
    obj.execute_all()
