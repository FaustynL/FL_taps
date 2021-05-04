import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from settings import testSettings
from pages import datepickerPage, basicAuth


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


