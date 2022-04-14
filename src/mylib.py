import time


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


def is_element_present(driver, xpath):
    # 从selenium.common.exceptions 模块导入 NoSuchElementException类
    from selenium.common.exceptions import NoSuchElementException
    try:
        element = driver.find_element_by_xpath(xpath)
    # 原文是except NoSuchElementException, e:
    except NoSuchElementException as e:
        # 打印异常信息
        print(e)
        return False
    else:
        # 没有发生异常，表示在页面中找到了该元素，返回True
        return True
def insert_data_to_major_score_line():
    pass