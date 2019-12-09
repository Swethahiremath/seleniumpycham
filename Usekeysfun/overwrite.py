from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
un=driver.find_element_by_id('username')
un.send_keys('admin')
driver.find_element_by_name('pwd').send_keys('manager')
#un.clear()
sleep(3)
un.send_keys(Keys.CONTROL+'a')
un.send_keys(Keys.DELETE)
un.send_keys('trainee')

sleep(10)
