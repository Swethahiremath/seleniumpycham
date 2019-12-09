from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.cleartrip.com/")
driver.implicitly_wait(20)
driver.find_element_by_class_name("//i[@class='icon.ir.datePicker'][1]").click()