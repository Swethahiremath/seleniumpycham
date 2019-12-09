from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.actitime.com/login.do")

driver.save_screenshot("actiloginpage.png")