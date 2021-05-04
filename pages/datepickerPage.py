from helpers.support_functions import *


datapickerTab = 'datepicker-header'
datapickerContent = 'datepicker-content'
chooseDate = '//*[@id="start"]'


def datePickerTab(driver_instance):
    wait_for_visibility_of_element(driver_instance, datapickerTab)
    elem = driver_instance.find_element_by_id(datapickerTab)
    elem.click()


def datapickerContentDisplayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, datapickerContent)
    return elem.is_displayed()

def chooseDateWindow(driver_instance):
    elem = driver_instance.find_element_by_xpath(chooseDate)
    sampleDate = "2020-07-22"
    if sampleDate == elem.get_attribute("value"):
        return True
    else:
        return False




