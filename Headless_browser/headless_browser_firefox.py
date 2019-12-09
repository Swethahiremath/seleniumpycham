from selenium import webdriver
from time import sleep

options1=webdriver.FirefoxOptions()

options1.headless=True

driver=webdriver.Firefox(options=options1)

driver.get("https://demo.actitime.com/login.do")


print("Browser is running")
sleep(3)
driver.close()