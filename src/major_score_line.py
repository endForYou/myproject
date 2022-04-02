# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from db import DataBase

db = DataBase().get_cursor()
caps = {"platformName": "Android", "appium:platformVersion": "11", "appium:deviceName": "Lenovo_L79031",
        "appium:appPackage": "com.eagersoft.youzy.youzy", "appium:appActivity": ".mvvm.ui.launch.LaunchActivity",
        "appium:ensureWebviewsHavePages": True, "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True, 'noReset': True, 'fullReset': False,
        'settings[waitForIdleTimeout]': 100}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

driver.implicitly_wait(10)

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
# WebDriverWait.until()
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, "myDynamicElement"))
# )
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(392, 2227)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(516, 551)
actions.w3c_actions.pointer_action.release()
actions.perform()
# 下拉的时候要判断这个院校是否已经点击,如果在就忽略，如果不在就执行，并把这个college加到college_list里去
college_list = []
college_name = ""
if college_name not in college_list:
    college_list.append(college_name)
time.sleep(3)
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

    driver.tap([(540, 238), ])
    # actions.perform()
    # 点击专业分数线
    # "<div class="_selected-element-table-cells_619e8">com.eagersoft.youzy.youzy:id/tab</div>"
    # "androidx.appcompat.app.ActionBar$Tab" tab2 专业分数线 tab3 招生计划
    # major_score_line_tab_el = \
    # el16=driver.find_elements(by=AppiumBy.CLASS_NAME, value="androidx.appcompat.app.ActionBar$Tab")[2]
    # el16.click()

    # 点击物理历史
    driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/material_spinner2_course").click()

    # 分数线切换

    grade_list = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")

    # 点击招生方向
    driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
    enroll_direction_list = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")
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
    # 点击本科专科
    driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/material_spinner2_batch").click()
    # 点击专科（默认本科）
    driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/tv_tinted_spinner")[
        1].click()
    # 点击招生方向

    driver.find_element(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/cl_college").click()
    enroll_direction_list = driver.find_elements(by=AppiumBy.ID, value="com.eagersoft.youzy.youzy:id/college_name")
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
    # 点击历史（默认物理）
db.close()
driver.quit()
