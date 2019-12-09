from selenium import webdriver
import time
driver=webdriver.Chrome("D:\Pythonpractice\seleniumeclipse\selenumpy\drivers\chromedriver\chromedriver.exe")
driver.maximize_window()
actual_url="https://demo.actitime.com/login.do"
driver.get(actual_url)
driver.get("https://www.facebook.com")
driver.back()
driver.forward()
title=driver.title
print('Title is',title)
if 'actiTime' in title:
    print('navigate back to the previous page successfully')
else:
    print('navigation back tot he previous page failed')
time.sleep(2)
driver.quit()