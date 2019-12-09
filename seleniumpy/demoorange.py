from selenium import webdriver
from selenium.webdriver.common import by
import time
driver=webdriver.Chrome("D:\Pythonpractice\seleniumeclipse\selenumpy\drivers\chromedriver\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername")
driver.find_element_by_id("txtPassword")
driver.find_element_by_name("Submit")

time.sleep(5)
driver.close()