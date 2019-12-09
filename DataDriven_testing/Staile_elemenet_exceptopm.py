from selenium import webdriver
from  time import sleep

driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")

username=driver.find_element_by_id("username")
pwd=driver.find_element_by_name("pwd")
login=driver.find_element_by_id("loginButton")


username.send_keys("admin")
pwd.send_keys("admin")
login.click()
sleep(5)

username.send_keys("admin")
pwd.send_keys("manager")
login.click()

driver.close()
