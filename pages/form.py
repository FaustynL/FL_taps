from helpers.support_functions import *


formTab = 'form-header'
formContent = 'form-content'
firstNameField = '//*[@id="fname"]'
lastNameField = '//*[@id="lname"]'
submitButton = '//*[@id="formSubmitButton"]'
notification = '//*[@id="basic-accordian"]/script[3]'
notificationMessage = '//*[@id="basic-accordian"]/script[3]/text()'


def formHeader(driver_instance):
    wait_for_visibility_of_element(driver_instance, formTab)
    elem = driver_instance.find_element_by_id(formTab)
    elem.click()


def formContentVisibility(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, formContent)
    return elem.is_displayed()


def enterName(driver_instance):
    elem = driver_instance.find_element_by_xpath(firstNameField)
    elem.send_keys("Adam")


def enterSurname(driver_instance):
    elem = driver_instance.find_element_by_xpath(lastNameField)
    elem.send_keys("Małysz")


def clickSubmit(driver_instance):
    elem = driver_instance.find_element_by_xpath(submitButton)
    elem.click()










