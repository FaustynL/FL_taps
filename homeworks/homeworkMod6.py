from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
url = 'https://fabrykatestow.pl'

driver.maximize_window()
mainPage = driver.get(url)
coursesPage = driver.find_element_by_xpath('//*[@id="menu-item-622"]/a')
coursesPage.click()
tapsPage = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[2]/div/div/div/div/section[1]/div/div/div[1]/div/div/div/div/div/a/span/span[2]')
tapsPage.click()
scrollTo = ActionChains(driver)
whoIsLearn = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/section[5]/div[1]')
scrollTo.move_to_element(whoIsLearn).perform()
sleep(5)
driver.get_screenshot_as_file('nauczyciel.png')


driver.close()