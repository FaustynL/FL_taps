from helpers.support_functions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.by import By
import subprocess


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


def drag_and_drop_helper(driver_instance):
    driver_instance.implicitly_wait(10)
    with open(os.path.abspath('../homeworks/native_js_drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()
    driver_instance.execute_script(script + "$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    sleep(2)

