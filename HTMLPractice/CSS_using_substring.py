from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https:actitime')

#find the element by providint the class name
driver.find_element_by_id('username').send_keys('admin')

driver.find_element_by_name('pwd').send_keys('manager')

#find element by using css substring Prefix ^
driver.find_element_by_css_selector("a[class^='initial']").click()

#find element using sufix with $
driver.find_element_by_css_selector("a[id$='nButton']").click()

#find element by using Sub string *
driver.find_element_by_css_selector("a[id*='inB']").click()
