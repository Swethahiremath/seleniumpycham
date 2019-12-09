from selenium import webdriver
import time
driver=webdriver.Chrome("D:\Pythonpractice\seleniumeclipse\selenumpy\drivers\chromedriver\chromedriver.exe")
#driver.maximize_window()
#time.sleep(2)
#driver.set_window_size(1000,1000)
#time.sleep(2)
#driver.set_window_position(400,600)
#time.sleep(2)
#driver.set_window_rect(600,400,600,600)
#time.sleep(2)
#driver.refresh()
driver.get("https://demo.actitime.com/login.do")

#CSS attributes with sinal input
#driver.find_element_by_css_selector("input[name='username")

#css attrributes with multiple attributes
#driver.find_element_by_css_selector("input[name=username][type=text]").send_keys("admin")
driver.find_element_by_css_selector("input[name=pwd][type=password").send_keys("manager")
#driver.find_element_by_css_selector("a[id=loginButton]").click()
#css attribute using id
driver.find_element_by_css_selector("a#loginButton").click()

#css attrivute using class name
#driver.find_element_by_css_selector("input.textField").send_keys("admin")


driver.find_element_by_css_selector("input[id=username]").send_keys("admin")


time.sleep(10)
driver.close()