from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get('https://www.google.co.in/')

#First idetify the name element which search the keys
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(2)

#To indentify the first list element
#driver.find_element_by_css_selector("ul li:first-child").click()

#To identify the 2nd list element
#driver.find_element_by_css_selector("ul li:Last-child").click()

#To identify the nth Child  element
#driver.find_element_by_css_selector("ul li:nth-child(4)").click()

#To identify the nth-of-child Child  element
#driver.find_element_by_css_selector("ul li:nth-of-type(4)").click()

#toidentify both nth-child or nth-of-child
#driver.find_element_by_css_selector("ul *:nth-of-type(4)").click()


time.sleep(2)
#driver.quit()