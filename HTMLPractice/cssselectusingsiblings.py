from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('D:\\Pythonpractice\\seleniumpycham\\HTMLPractice\\Formpageonsameline.html')

#driver.find_element_by_css_selector("input#username+input+input").send_keys("Swetha")
driver.find_element_by_css_selector("input#username+input").send_keys("swetha")

time.sleep(3)