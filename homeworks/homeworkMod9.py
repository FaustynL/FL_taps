import unittest
from selenium import webdriver
from settings import testSettings
from pages import datepickerPage, basicAuth, form, keyPress, dragAndDrop, statusCodes, iFrame





class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
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

    def test6_statusCode200_test(self):
        statusCodes.statusCodesHeader(self.driver)
        self.assertTrue(statusCodes.codesContentVisibility(self.driver))
        statusCodes.clickCode200(self.driver)
        self.assertTrue(statusCodes.pagesStatus200Check(self.driver))

    def test7_statusCode305_test(self):
        statusCodes.statusCodesHeader(self.driver)
        self.assertTrue(statusCodes.codesContentVisibility(self.driver))
        statusCodes.clickCode305(self.driver)
        self.assertTrue(statusCodes.pagesStatus305Check(self.driver))

    def test8_statusCode404_test(self):
        statusCodes.statusCodesHeader(self.driver)
        self.assertTrue(statusCodes.codesContentVisibility(self.driver))
        statusCodes.clickCode404(self.driver)
        self.assertTrue(statusCodes.pagesStatus404Check(self.driver))

    def test9_statusCode500_test(self):
        statusCodes.statusCodesHeader(self.driver)
        self.assertTrue(statusCodes.codesContentVisibility(self.driver))
        statusCodes.clickCode500(self.driver)
        self.assertTrue(statusCodes.pagesStatus500Check(self.driver))

    def test10_iFrame1_test(self):
        iFrame.iFrameHeader(self.driver)
        self.assertTrue(iFrame.iFrameContent(self.driver))
        iFrame.clickButtonOne(self.driver)
        self.assertTrue(iFrame.checkMessage(self.driver))

    def test11_iFrame2_test(self):
        iFrame.iFrameHeader(self.driver)
        self.assertTrue(iFrame.iFrameContent(self.driver))
        iFrame.clickButtonTwo(self.driver)
        self.assertTrue(iFrame.checkMessage(self.driver))

if __name__ == '__main__':
    unittest.main()
