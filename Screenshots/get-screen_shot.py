from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.actitime.com/login.do")
sleep(3)

driver.get_screenshot_as_file("D:\\activilogin.png")

sleep(3)

driver.close()