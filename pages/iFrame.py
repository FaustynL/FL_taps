from helpers.support_functions import *
from selenium.webdriver.support.ui import WebDriverWait as wait

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
frame_id = '//*[@id="iframe-content"]/div/div/iframe'
button_1 = '//*[@id="simpleButton1"]'
button_2 = '//*[@id="simpleButton2"]'
button_check = '//*[@id="whichButtonIsClickedMessage"]'


def iFrameHeader(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_tab)
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iFrameContent(driver_instance):
    wait_for_visibility_of_element(driver_instance, iframe_content)
    elem = driver_instance.find_element_by_id(iframe_content)
    return elem.is_displayed()


#def switchToFrame(driver_instance):
#   wait_for_visibility_of_element_by_xpath(driver_instance, frame_id)
#   driver_instance.switch_to.frame(driver_instance.find_element_by_xpath(frame_id))



def clickButtonOne(driver_instance):
    wait(driver_instance, 10).until(EC.frame_to_be_available_and_switch_to_it(driver_instance.find_element_by_xpath(frame_id)))
    elem = driver_instance.find_element_by_xpath(button_1)
    elem.click()


def clickButtonTwo(driver_instance):
    wait(driver_instance, 10).until(EC.frame_to_be_available_and_switch_to_it(driver_instance.find_element_by_xpath(frame_id)))
    elem = driver_instance.find_element_by_xpath(button_2)
    elem.click()


def checkMessage(driver_instance):
    elem = driver_instance.find_element_by_xpath(button_check)
    button_msg_1 = '1'
    button_msg_2 = '2'
    whichButton = elem.text
    array = whichButton.split(' ')
    if array[1] == button_msg_1:
        return True
    elif array[1] == button_msg_2:
        return True
    else:
        return False
