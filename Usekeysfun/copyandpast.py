from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
un = driver.find_element_by_id('username')
un.send_keys('trainee')
un.send_keys(Keys.CONTROL,'a','c')
pw=driver.find_element_by_name('pwd')
pw.send_keys(Keys.CONTROL,'v')
driver.find_element_by_xpath("//a[@id='loginButton']").send_keys(Keys.ENTER)
sleep(3)
driver.quit()