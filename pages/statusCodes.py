from helpers.support_functions import *

status_codes_tab = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
code_200 = '//*[@id="200siteAnchor"]'
code200_message = '/html/body/pre'
code_305 = '//*[@id="305siteAnchor"]'
code305_message = '/html/body/pre'
code_404 = '//*[@id="404siteAnchor"]'
code404_message = '/html/body/pre'
code_500 = '//*[@id="500siteAnchor"]'
code500_message = '/html/body/pre'


def statusCodesHeader(driver_instance):
    wait_for_visibility_of_element(driver_instance, status_codes_tab)
    elem = driver_instance.find_element_by_id(status_codes_tab)
    elem.click()


def codesContentVisibility(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, status_codes_content)
    return elem.is_displayed()


def clickCode200(driver_instance):
    wait_for_visibility_of_element(driver_instance, code_200)
    elem = driver_instance.find_element_by_xpath(code_200)
    elem.click()


def pagesStatus200Check(driver_isntance):
    wait_for_visibility_of_element_by_xpath(driver_isntance, code200_message)
    elem = driver_isntance.find_element_by_xpath(code200_message)
    expected_message = '200 OK'
    if elem.text == expected_message:
        return True
    else:
        return False


def clickCode305(driver_instance):
    wait_for_visibility_of_element(driver_instance, code_305)
    elem = driver_instance.find_element_by_xpath(code_305)
    elem.click()


def pagesStatus305Check(driver_isntance):
    wait_for_visibility_of_element_by_xpath(driver_isntance, code305_message)
    elem = driver_isntance.find_element_by_xpath(code305_message)
    expected_message = '305 Use Proxy'
    if elem.text == expected_message:
        return True
    else:
        return False


def clickCode404(driver_instance):
    wait_for_visibility_of_element(driver_instance, code_404)
    elem = driver_instance.find_element_by_xpath(code_404)
    elem.click()


def pagesStatus404Check(driver_isntance):
    wait_for_visibility_of_element_by_xpath(driver_isntance, code404_message)
    elem = driver_isntance.find_element_by_xpath(code404_message)
    expected_message = '404 Not Found'
    if elem.text == expected_message:
        return True
    else:
        return False


def clickCode500(driver_instance):
    wait_for_visibility_of_element(driver_instance, code_500)
    elem = driver_instance.find_element_by_xpath(code_500)
    elem.click()


def pagesStatus500Check(driver_isntance):
    wait_for_visibility_of_element_by_xpath(driver_isntance, code500_message)
    elem = driver_isntance.find_element_by_xpath(code500_message)
    expected_message = '500 Internal Server Error'
    if elem.text == expected_message:
        return True
    else:
        return False
