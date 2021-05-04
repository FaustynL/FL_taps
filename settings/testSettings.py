from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
pageUrl = 'http://simpletestsite.fabrykatestow.pl/'