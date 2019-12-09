from selenium import webdriver
from time import sleep

options1=webdriver.ChromeOptions()

options1.headless=True

driver=webdriver.Chrome(options=options1)
driver.get("https://demo.actitime.com/login.do")
sleep(4)
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id("pwd").send_keys("manager")

driver

driver.close()