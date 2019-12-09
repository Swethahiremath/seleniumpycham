from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
#driver.get('D:\\Pythonpractice\\seleniumpycham\\HTMLPractice\\Loginformpage1.html')
#driver.find_element_by_name("username").send_keys("Swetha")
#driver.find_element_by_id("text password").send_keys('Swetha')

#driver.find_element_by_css_selector("input[id=Submit]").click()

driver.get('D:\\Pythonpractice\\seleniumpycham\\HTMLPractice/Listpage.html')

#Select a immediate parent elements
#driver.find_element_by_css_selector("ul#parent>li")

#select a set of parent and child
driver.find_element_by_css_selector("ul#parent li")

time.sleep(3)
driver.quit()