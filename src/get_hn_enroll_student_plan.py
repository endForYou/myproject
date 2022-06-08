from appium import webdriver
from mylib import *
import db
from src.base import Base


class HnEnrollStudentPlanLine(Base):

    # def execute_one_tab_enroll_plan(self):
    #     """
    #     暂时不需要了，因为数据一次性就加载出来了
    #     :return:
    #     """
    #     driver = self.driver
    #     if is_element_exist(driver, element="com.eagersoft.youzy.youzy:id/cl_college"):
    #         enroll_direction_list_count = len(
    #             list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")))
    #         for i in range(0, enroll_direction_list_count):
    #             driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
    #             enroll_direction = \
    #                 driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")[i]
    #             # 点击某个招生方向
    #             enroll_direction.click()
    #             # 最后需要关闭招生方向的toast
    #             driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_close").click()

    def execute_ben(self):
        self.execute_ben_of_ngk()
        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        province="湖南"
        colleges = get_all_colleges(cursor, province=province, data_type="enroll_plan")
        no_need_colleges = get_all_colleges_of_no_need(cursor, province=province, data_type="enroll_plan")
        for i in range(0, 500):
            self.get_one_page_enroll_plan_of_ben_ngk(colleges, no_need_colleges, province)
            self.next_page()
        self.driver.quit()


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
    obj = HnEnrollStudentPlanLine(my_driver)
    obj.execute_all()
