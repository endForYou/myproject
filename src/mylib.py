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
