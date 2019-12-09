from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_name('pwd').send_keys('manager')
driver.find_element_by_xpath("//a[@id='loginButton']").send_keys(Keys.ENTER)
sleep(10)
driver.close()