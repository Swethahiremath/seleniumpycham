from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get('https://www.google.com')
driver.maximizer()
driver.close()