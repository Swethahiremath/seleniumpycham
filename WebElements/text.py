from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://demo.actitime.com/login.do")
link=driver.find_element_by_link_text("Forgot your password?")

toe=link.text
print("Text of element is",toe)
driver.quit()


