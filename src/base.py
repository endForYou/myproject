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

    def execute_zhuan_of_ngk(self):
        driver = self.driver

        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_logo")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_filter").click()
        # 点击专科
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/batch").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[1].click()
        driver.find_element(by=AppiumBy.ID,
                            value="com.eagersoft.youzy.youzy:id/click_confirm").click()

    def execute_zhuan_of_ogk(self):
        driver = self.driver

        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()

        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_filter").click()
        # 点击专科
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/batch").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[2].click()
        driver.find_element(by=AppiumBy.ID,
                            value="com.eagersoft.youzy.youzy:id/click_confirm").click()

    def execute_ben_of_ogk(self):
        driver = self.driver

        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        # 本科
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_filter").click()
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/batch").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[1].click()
        driver.find_element(by=AppiumBy.ID,
                            value="com.eagersoft.youzy.youzy:id/click_confirm").click()

    def execute_ben_of_ngk(self):
        driver = self.driver
        time.sleep(10)
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/iv_logo")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        # 本科
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_filter").click()
        driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/batch").find_elements(
            by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/textView")[1].click()
        driver.find_element(by=AppiumBy.ID,
                            value="com.eagersoft.youzy.youzy:id/click_confirm").click()

    def get_one_page_enroll_plan_of_ben_ngk(self, colleges, no_need_colleges, province):
        driver = self.driver
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        data_type = "enroll_plan"
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
                if college_name in no_need_colleges or college_name in colleges or college_name in self.college_list:
                    continue
                college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_enter_plan")
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
                self.college_list.append(title_college_name)
                # 这里不用点击，因为会直接到招生计划这里
                # 如果年份没有，则直接返回
                # 暂时注释掉这句
                # if not is_element_present(self.driver,
                #                           "com.eagersoft.youzy.youzy:id/material_spinner_year"):
                #     # 如果这里没加载出来，直接返回
                #     # 点击从招生计划回退
                #     # 把college_name 写进数据库
                #     insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=1)
                #     back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                #     back_element.click()
                #     # 点击从院校详情回退回退
                #     back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                #     back_element.click()
                #     continue
                # 如果返回为空，也直接返回
                # if is_element_present(self.driver, "com.eagersoft.youzy.youzy:id/emptyStateContentTextView"):
                if not is_element_present(self.driver,"com.eagersoft.youzy.youzy:id/tv_choose:"):
                    insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=1)
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                    back_element.click()
                    # 点击从院校详情回退回退
                    back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                    back_element.click()
                    continue
                insert_data_to_yzy_college(cursor, title_college_name, province, data_type, is_no_need_crawl=None)
                time.sleep(1)
                course_text = driver.find_element(by=AppiumBy.ID,
                                                  value="com.eagersoft.youzy.youzy:id/material_spinner2_course").text.strip()
                if course_text == "物理":
                    # 默认
                    grade = "本科"
                    science_art = "物理"

                    grade = "本科"
                    science_art = "历史"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        1].click()
                else:
                    # 默认
                    grade = "本科"
                    science_art = "历史"

                    grade = "本科"
                    science_art = "物理"
                    driver.find_element(by=AppiumBy.ID,
                                        value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()
                    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
                        0].click()
                # 点击从专业分数线回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/leftBackImg")
                back_element.click()
                # 点击从院校详情回退回退
                back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
                back_element.click()

    def get_one_page_major_score_line_of_ben_gk(self, colleges, no_need_colleges, province):
        my_db = db.DataBase()
        cursor = my_db.get_cursor()
        driver = self.driver

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
