from selenium import webdriver
import time
driver=webdriver.Firefox(executable_path="D:\Pythonpractice\seleniumeclipse\selenumpy\drivers\geckodriver\geckodriver.exe")
driver.get('https://www.google.com')
driver.close()
