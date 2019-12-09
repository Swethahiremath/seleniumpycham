from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")

name=driver.find_element_by_css_selector("input#username")
name.send_keys("admin")

pwd=driver.find_element_by_css_selector("input.textField.pwdfield")
pwd.send_keys("manager")

print('Value present in the name text filed is',name.get_attribute("value"))
print('Value present in the password filed is',pwd.get_attribute("value"))
print('Id value for the  username attribute filed is',name.get_attribute("id"))
print('Name value for the password field attribute is ',pwd.get_attribute("name"))
driver.close()
