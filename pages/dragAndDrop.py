from helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains


drag_and_drop_tab = 'draganddrop-header'
drag_and_drop_content = 'draganddrop-content'
square_a = '//*[@id="column-a"]'
square_b = '//*[@id="column-b"]'


def dragAndDropHeader(driver_instance):
    wait_for_visibility_of_element(driver_instance, drag_and_drop_tab)
    elem = driver_instance.find_element_by_id(drag_and_drop_tab)
    elem.click()


def dragAndDropContentVisibility(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, drag_and_drop_content)
    return elem.is_displayed()


def dragAndDropSquareA(driver_instance):
    wait_for_visibility_of_element(driver_instance, square_a)
    elem = driver_instance.find_element_by_xpath(square_a)
    elemb = driver_instance.find_element_by_xpath(square_b)
    ActionChains(driver_instance).drag_and_drop(elem, elemb).perform()





