import time

import pytest
import os
import textwrap
import copy

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

from helpers import report_to_sauce, take_screenshot_and_logcat, ANDROID_BASE_CAPS, EXECUTOR


class TestAndroidBasicInteractions:
    # PACKAGE = 'io.appium.android.apis'
    # SEARCH_ACTIVITY = '.app.SearchInvoke'
    # ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'

    @pytest.fixture(scope='function')
    def driver(self, request, device_logger):
        calling_request = request._pyfuncitem.name

        caps = copy.copy(ANDROID_BASE_CAPS)
        caps['noReset'] = True
        caps['fullReset'] = False

        driver = webdriver.Remote(
            command_executor=EXECUTOR,
            desired_capabilities=caps
        )

        def fin():
            report_to_sauce(driver.session_id)
            take_screenshot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)

        driver.implicitly_wait(10)
        return driver

    def traverse_enroll_direction(self,enroll_direction_list,driver):
        for enroll_direction in enroll_direction_list:
            # 点击某个招生方向
            enroll_direction.click()
            # 专业分数线列表
            major_score_line_list_element = driver.find_element(by=AppiumBy.ID,
                                                                value="com.eagersoft.youzy.youzy:id/recycler_view")
            for major_score_line_element in major_score_line_list_element.find_elements(by=AppiumBy.ID,
                                                                                        value="com.eagersoft.youzy.youzy:id"
                                                                                              "/parent"):
                # print(major_score_line_element, 1111111111)
                major_name = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                   value="com.eagersoft.youzy.youzy:id/tv_major_name").text
                subject_need = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_choose").text
                enroll_count = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_enrollment").text
                highest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                      value="com.eagersoft.youzy.youzy:id/tv_score").text
                lowest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_seating").text
                print(major_name)
                print(subject_need)
                print(enroll_count)
                print(highest_score)
                print(lowest_score)
            driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
    def test_major_score_line(self, driver):
        # 点击同意隐私政策
        # agree_policy_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/okey")
        # agree_policy_element.click()
        # # 点击打开yzy
        # open_yzy_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_btn_open_youzy")
        # open_yzy_element.click()
        # # 为了简化脚本，这里需要手动登陆，最好是等待30s以上
        # # time.sleep(90)
        # # el3 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/rightImgMenu")
        # # el3.click()
        # # 点击关掉弹窗
        # # 点击不同意获取位置信息
        driver.implicitly_wait(120)
        # dialog_element = driver.find_element(by=AppiumBy.ID,
        #                                      value="com.eagersoft.youzy.youzy:id/click_close_dialog_activity_pop")
        # dialog_element.click()
        # donot_agree_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cancel")
        # donot_agree_element.click()
        # 点击找大学
        find_college_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/ll_btn_zdx")
        find_college_element.click()
        # 点击查所有大学
        find_all_college_element = driver.find_element(by=AppiumBy.ID,
                                                       value="com.eagersoft.youzy.youzy:id/click_all_college")
        find_all_college_element.click()
        # # list列表
        time.sleep(5)
        college_list_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/recycleView")
        for college_element in college_list_element.find_elements(by=AppiumBy.ID,
                                                                  value="com.eagersoft.youzy.youzy:id/menu"):
            college_element.click()
            el15 = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_history")
            el15.click()
            # actions = ActionChains(driver)
            # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # actions.w3c_actions.pointer_action.move_to_location(540, 238)
            # actions.w3c_actions.pointer_action.pointer_down()
            # actions.w3c_actions.pointer_action.pause(0.1)
            # actions.w3c_actions.pointer_action.release()
            time.sleep(5)
            driver.tap([(540, 238), ])
            # actions.perform()
            # 点击专业分数线
            # "<div class="_selected-element-table-cells_619e8">com.eagersoft.youzy.youzy:id/tab</div>"
            # "androidx.appcompat.app.ActionBar$Tab" tab2 专业分数线 tab3 招生计划
            # major_score_line_tab_el = \
            # el16=driver.find_elements(by=AppiumBy.CLASS_NAME, value="androidx.appcompat.app.ActionBar$Tab")[2]
            # el16.click()
            time.sleep(5)
            major_score_line_list_element = driver.find_element(by=AppiumBy.ID,
                                                                value="com.eagersoft.youzy.youzy:id/recycler_view")
            for major_score_line_element in major_score_line_list_element.find_elements(by=AppiumBy.ID,
                                                                                        value="com.eagersoft.youzy.youzy:id/parent"):
                print(major_score_line_element,1111111111)
                major_name = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                   value="com.eagersoft.youzy.youzy:id/tv_major_name").text
                subject_need = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_choose").text
                enroll_count = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_enrollment").text
                highest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                      value="com.eagersoft.youzy.youzy:id/tv_score").text
                lowest_score = major_score_line_element.find_element(by=AppiumBy.ID,
                                                                     value="com.eagersoft.youzy.youzy:id/tv_seating").text
                print(major_name)
                print(subject_need)
                print(enroll_count)
                print(highest_score)
                print(lowest_score)
        # 点击某所大学
        # el14 = driver.find_element(by=AppiumBy.CLASS_NAME,
        #                            value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.view.ViewGroup")
        # el14.click()
        # # 点击历史分数线

        # el16 = driver.find_element(by=AppiumBy.CLASS_NAME,
        #                            value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/androidx.appcompat.app.ActionBar.Tab[2]/android.widget.TextView")
        # el16.click()
        # # 切换不同的组合
        # # 分数列表
        # "com.eagersoft.youzy.youzy:id/view_pager"
        #
        # # 点击从专业分数线回退
        # "com.eagersoft.youzy.youzy:id/leftBackImg"
        # # 点击从院校详情回退回退
        # back_element = driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/click_back")
        # back_element.click()
        #
        # search_text = driver.find_element(By.ID, 'android:id/search_src_text')
        # search_text_value = search_text.text
        #
        # assert 'Hello world!' == search_text_value

    # def test_should_click_a_button_that_opens_an_alert_and_then_dismisses_it(self, driver):
    #     driver.start_activity(self.PACKAGE, self.ALERT_DIALOG_ACTIVITY)
    #
    #     open_dialog_button = driver.find_element(By.ID, 'io.appium.android.apis:id/two_buttons')
    #     open_dialog_button.click()
    #
    #     alert_element = driver.find_element(By.ID, 'android:id/alertTitle')
    #     alert_text = alert_element.text
    #
    #     assert textwrap.dedent('''\
    #     Lorem ipsum dolor sit aie consectetur adipiscing
    #     Plloaso mako nuto siwuf cakso dodtos anr koop.''') == alert_text
    #
    #     close_dialog_button = driver.find_element(By.ID, 'android:id/button1')
    #     close_dialog_button.click()
