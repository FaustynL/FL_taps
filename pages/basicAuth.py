from helpers.support_functions import *


basicAuthTab = 'basicauth-header'
basicAuthContent = 'basicauth-content'
dataToLogin = '//*[@id="basicauth-content"]/div/p[1]'
usernameField = '//*[@id="ba_username"]'
usernamePassword = '//*[@id="ba_password"]'
loginButton = '//*[@id="content"]/button'
welcomeMessage = '//*[@id="loggedInMessage"]'


def basicAuthHeader(driver_instance):
    wait_for_visibility_of_element(driver_instance, basicAuthTab)
    elem = driver_instance.find_element_by_id(basicAuthTab)
    elem.click()


def basicAuthContentVisibility(driver_instance):
    wait_for_visibility_of_element(driver_instance, basicAuthContent)
    elem = driver_instance.find_element_by_id(basicAuthContent)
    return elem.is_displayed()


def usernameLogin(driver_instance):
    elem = driver_instance.find_element_by_xpath(dataToLogin)
    userLogin = elem.text
    array = userLogin.split(' ')
    return array[1]

def userPassword(driver_instance):
    elem = driver_instance.find_element_by_xpath(dataToLogin)
    userPass = elem.text
    array = userPass.split(' ')
    return array[4]


def enterUsername(driver_instance):
    elem = driver_instance.find_element_by_xpath(usernameField)
    elem.send_keys(usernameLogin(driver_instance))


def enterUserPassword(driver_instance):
    elem = driver_instance.find_element_by_xpath(usernamePassword)
    elem.send_keys(userPassword(driver_instance))


def clickLoginButton(driver_instance):
    elem = driver_instance.find_element_by_xpath(loginButton)
    elem.click()


def userIsLogged(driver_instance):
    elem = driver_instance.find_element_by_xpath(welcomeMessage)
    welcoming_message = "You are logged in!"
    if welcoming_message == elem.text:
        return True
    else:
        return False







