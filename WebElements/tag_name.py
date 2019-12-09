from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
webele=driver.find_element_by_link_text("Forgot your password?")
sleep(2)

print('The tagname of the webelement is',webele.tag_name)

driver.quit()