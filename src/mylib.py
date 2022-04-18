import time

import pymysql.cursors
from appium.webdriver.common.appiumby import AppiumBy
from db import *


def is_element_exist(driver, element, timeout=1):
    count = 0
    while count < timeout:
        source = driver.page_source
        if element in source:
            return True
        else:
            count += 1
            time.sleep(1)
    return False


def is_element_present(driver, element_id):
    # 从selenium.common.exceptions 模块导入 NoSuchElementException类
    from selenium.common.exceptions import NoSuchElementException
    try:
        element = driver.find_element(by=AppiumBy.ID, value=element_id)
    # 原文是except NoSuchElementException, e:
    except NoSuchElementException as e:
        # 打印异常信息
        print(e)
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True


def is_element_present_by_element(element, element_id):
    # 从selenium.common.exceptions 模块导入 NoSuchElementException类
    from selenium.common.exceptions import NoSuchElementException
    try:
        element = element.find_element(by=AppiumBy.ID, value=element_id)
    # 原文是except NoSuchElementException, e:
    except NoSuchElementException as e:
        # 打印异常信息
        print(e)
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True


def insert_data_to_major_score_line(cursor: pymysql.cursors.DictCursor, params: [list, set]):
    insert_sql = """
    insert into yzy_major_score_ngk(major_name,subject_need,enroll_count,highest_score,lowest_score,college_name,
    college_direction,year,science_art,grade)
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cursor.executemany(insert_sql, params)


def get_all_colleges(cursor: pymysql.cursors.DictCursor):
    sql = "select distinct college_name from yzy_major_score_ngk"
    cursor.execute(sql)
    result = cursor.fetchall()
    res = []
    for data in result:
        college_name = data['college_name']
        res.append(college_name)
    return res
