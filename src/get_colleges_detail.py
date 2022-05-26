from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from appium import webdriver

from mylib import *
import db
from src.base import Base


class CollegesDetails(Base):

    def execute_all(self):
        """
        如果一次性没跑完，可能需要跑的时候先翻页
        :return:
        """
        self.enter_into_main_page_()
        # my_db = db.DataBase()
        # cursor = my_db.get_cursor()
        colleges = []
        # for i in range(0, 250):
        #     self.next_page()

        for i in range(0, 500):
            self.get_details(colleges)
            self.next_page()

        self.driver.quit()

    def get_details(self, colleges):
        driver = self.driver
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")))
        # print(driver.page_source)
        for i in range(0, college_list_element_count):
            college_element = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")[i]
            if not is_element_present_by_element(college_element, "com.eagersoft.youzy.youzy:id/name"):
                college_element.click()
                time.sleep(1)
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()
            else:
                college = college_element.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name").text
                college_name = college.split(" ")[0]
                # if college_name in colleges:
                #     continue
                if college_name not in self.college_list:
                    self.college_list.append(college_name)
                else:
                    continue
                college_element.click()
                # 点击从院校详情回退回退
                time.sleep(1)
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
    obj = CollegesDetails(my_driver)
    obj.execute_all()
