from helpers.support_functions import *
from selenium.webdriver.common.keys import Keys


keypress_tab = 'keypresses-header'
keypress_content = 'keypresses-content'
press_keys = '//*[@id="target"]'
press_key_result = 'keyPressResult'



def keypress_header(driver_instance):
    wait_for_visibility_of_element(driver_instance, keypress_tab)
    elem = driver_instance.find_element_by_id(keypress_tab)
    elem.click()


def keypress_content_visibility(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, keypress_content)
    return elem.is_displayed()


def press_enter(driver_instance):
    elem = driver_instance.find_element_by_xpath(press_keys)
    elem.send_keys(Keys.ENTER)


def key_press_result(driver_instance):
    wait_for_visibility_of_element(driver_instance, press_key_result)
    elem = driver_instance.find_element_by_id(press_key_result)
    expected_result = 'You entered: ENTER'
    if elem.text == expected_result:
        return True
    else:
        return False
