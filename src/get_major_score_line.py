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
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        time.sleep(3)
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        for i in range(0, 150):
            self.next_page()
        while True:
            if self.is_repeat_page():
                break
            self.get_one_page_major_score_line(cursor)
            # print(111111)
            self.next_page()

        self.driver.quit()

    def is_repeat_page(self):
        college_elements = self.driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name")
        for college in college_elements:
            college_name = college.text
            if college_name not in self.college_list:
                return False
        return True

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

    def execute_one_tab_major_score_line(self, cursor, college_name, grade, science_art):
        driver = self.driver

        time.sleep(1)
        if is_element_exist(driver, element="com.eagersoft.youzy.youzy:id/cl_college"):
            time.sleep(1)
            if is_element_exist(driver, element="com.eagersoft.youzy.youzy:id/cl_college"):
                time.sleep(1)
                driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
                enroll_direction_list_count = len(
                    list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")))
                for i in range(0, enroll_direction_list_count):
                    enroll_direction = \
                        driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")[i]
                    enroll_direction_name = enroll_direction.text
                    # 点击某个招生方向
                    # print(driver.page_source)
                    enroll_direction.click()
                    # 专业分数线列表

                    major_name_list = []

                    while True:
                        if self.is_repeat_detail_page(major_name_list):
                            break
                        add_major_name_list = self.get_one_tab_major_score_line(major_name_list, cursor, college_name,
                                                                                enroll_direction_name, grade,
                                                                                science_art)
                        major_name_list.extend(add_major_name_list)
                        # print(major_name_list)
                        # print(add_major_name_list)
                        self.next_page()
                    time.sleep(1)
                    driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
                    # 点击close
                    # 最后需要关闭招生方向的toast
                    time.sleep(1)
        else:
            if not is_element_present(driver, "com.eagersoft.youzy.youzy:id/emptyViewRelativeLayout"):
                major_name_list = []

                while True:
                    if self.is_repeat_detail_page(major_name_list):
                        break
                    enroll_direction_name = ""
                    add_major_name_list = self.get_one_tab_major_score_line(major_name_list, cursor, college_name,
                                                                            enroll_direction_name, grade, science_art)
                    major_name_list.extend(add_major_name_list)
                    # print(major_name_list)
                    # print(add_major_name_list)
                    self.next_page()

        if is_element_exist(driver, "com.eagersoft.youzy.youzy:id/iv_close"):
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_close").click()

    def get_one_tab_major_score_line(self, major_list, cursor, college_name, enroll_direction_name, grade, science_art):
        driver = self.driver
        major_score_line_list_element = driver.find_element(by=AppiumBy.ID,
                                                            value="com.eagersoft.youzy.youzy:id/recycler_view")
        params = set()
        year = 2021
        new_major_list = []
        for major_score_line_element in major_score_line_list_element.find_elements(by=AppiumBy.ID,
                                                                                    value="com.eagersoft.youzy.youzy:id"
                                                                                          "/parent"):
            if not is_element_present_by_element(major_score_line_element,
                                                 "com.eagersoft.youzy.youzy:id/tv_major_name"):
                continue
            major_name = major_score_line_element.find_element(by=AppiumBy.ID,
                                                               value="com.eagersoft.youzy.youzy:id/tv_major_name").text
            if major_name not in major_list:
                new_major_list.append(major_name)
            else:
                new_major_list.append(major_name)
                continue
            if not is_element_present_by_element(major_score_line_element,
                                                 "com.eagersoft.youzy.youzy:id/tv_choose") or not \
                    is_element_present_by_element(
                        major_score_line_element,
                        "com.eagersoft.youzy.youzy:id/tv_enrollment") or not is_element_present_by_element(
                major_score_line_element, "com.eagersoft.youzy.youzy:id/tv_score") or not is_element_present_by_element(
                major_score_line_element, "com.eagersoft.youzy.youzy:id/tv_seating"):
                continue
            subject_need = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                 value="com.eagersoft.youzy.youzy:id/tv_choose").text
            enroll_count = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                 value="com.eagersoft.youzy.youzy:id/tv_enrollment").text
            highest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                  value="com.eagersoft.youzy.youzy:id/tv_score").text
            lowest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                 value="com.eagersoft.youzy.youzy:id/tv_seating").text
            # 循环的最后需要再次点击招生方向切换
            params.add((major_name, subject_need, enroll_count, highest_score, lowest_score, college_name,
                        enroll_direction_name, year, science_art, grade))
        insert_data_to_major_score_line(cursor, params)
        return new_major_list

    def get_one_page_major_score_line(self, cursor):
        driver = self.driver
        college_list_element_count = len(
            list(driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")))
        # print(driver.page_source)
        colleges = get_all_colleges(cursor)
        for i in range(0, college_list_element_count):

            college_element = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/menu")[i]
            if not is_element_present_by_element(college_element, "com.eagersoft.youzy.youzy:id/name"):
                college_element.click()
                college_name = ""
            else:
                college = college_element.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/name").text
                college_name = college.split(" ")[0]
                print(college_name)
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
            driver.tap([(540, 238), ])
            title_college_name = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/title").text
            if title_college_name in colleges:
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()
            else:
                # 点击招生方向,先判断有没有招生方向
                grade = "本科"
                science_art = "历史"
                self.execute_one_tab_major_score_line(cursor, college_name, grade, science_art)
                # 点击本科专科
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                # 点击专科（默认本科）
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    1].click()
                grade = "专科"
                science_art = "历史"
                self.execute_one_tab_major_score_line(cursor, college_name, grade, science_art)
                # 点击历史（默认物理）
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    0].click()
                grade = "专科"
                science_art = "物理"
                self.execute_one_tab_major_score_line(cursor, college_name, grade, science_art)
                # 点击本科专科
                driver.find_element(by=AppiumBy.ID,
                                    value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
                # 点击本科
                driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                    0].click()
                # 点击招生方向
                grade = "本科"
                science_art = "物理"
                self.execute_one_tab_major_score_line(cursor, college_name, grade, science_art)
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
            'settings[waitForIdleTimeout]': 10,
            "automationName": "UiAutomator2"}
    my_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    my_driver.implicitly_wait(10)
    obj = MajorScoreLine(my_driver)
    obj.execute_all()
