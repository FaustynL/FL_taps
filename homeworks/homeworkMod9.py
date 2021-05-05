import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from settings import testSettings
from pages import datepickerPage, basicAuth, form, keyPress, dragAndDrop
from time import sleep



class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url = testSettings.pageUrl
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test1_datepickerPage_test(self):
        datepickerPage.datePickerTab(self.driver)
        self.assertTrue(datepickerPage.datapickerContentDisplayed(self.driver))
        datepickerPage.chooseDateWindow(self.driver)
        self.assertTrue(datepickerPage.chooseDateWindow(self.driver))

    def test2_basicAuth_test(self):
        basicAuth.basicAuthHeader(self.driver)
        self.assertTrue(basicAuth.basicAuthContentVisibility(self.driver))
        basicAuth.enterUsername(self.driver)
        basicAuth.enterUserPassword(self.driver)
        basicAuth.clickLoginButton(self.driver)
        self.assertTrue(basicAuth.userIsLogged(self.driver))

    def test3_form_test(self):
        form.formHeader(self.driver)
        self.assertTrue(form.formContentVisibility(self.driver))
        form.enterName(self.driver)
        form.enterSurname(self.driver)
        form.clickSubmit(self.driver)
        if self.assertTrue(self.driver.switch_to.alert.text) == 'success':
            self.driver.switch_to.alert.accept()
        else:
            False

    def test4_keyPress_test(self):
        keyPress.keypress_header(self.driver)
        self.assertTrue(keyPress.keypress_content_visibility(self.driver))
        keyPress.press_enter(self.driver)
        self.assertTrue(keyPress.key_press_result(self.driver))

    def test5_draganddrop_test(self):
        dragAndDrop.dragAndDropHeader(self.driver)
        self.assertTrue(dragAndDrop.dragAndDropContentVisibility(self.driver))
        self.assertTrue(dragAndDrop.dragAndDropSquareA(self.driver))




