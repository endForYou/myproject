# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
from telnetlib import EC

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from mylib import *
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
        'settings[waitForIdleTimeout]': 10}
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

# 下拉的时候要判断这个院校是否已经点击,如果在就忽略，如果不在就执行，并把这个college加到college_list里去
college_list = []

time.sleep(3)




# 执行完第一次8个学校后开始下拉刷新
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(392, 2227)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(516, 551)
actions.w3c_actions.pointer_action.release()
actions.perform()
db.close()
driver.quit()

# 招生计划
# code com.eagersoft.youzy.youzy:id/tv_code
# major_name com.eagersoft.youzy.youzy:id/tv_college
# subject com.eagersoft.youzy.youzy:id/tv_choose
# plan com.eagersoft.youzy.youzy:id/tv_plan
# schooling  com.eagersoft.youzy.youzy:id/tv_schooling
# cost com.eagersoft.youzy.youzy:id/tv_cost
