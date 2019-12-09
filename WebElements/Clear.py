from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
user_name = driver.find_element_by_id("email")
user_name.send_keys("admin")
user_pwd = driver.find_element_by_name("pass")
user_pwd.send_keys("manager")
user_name.clear()
sleep(3)
login_button=driver.find_element_by_xpath("//input[@value='Log In']")
login_button.submit()


