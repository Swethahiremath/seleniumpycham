from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
link=driver.find_element_by_link_text("Forgot your password?")
sleep(2)
if link.is_enabled():
    print('link is enabled')
else:
    print('link is not enabled')

driver.quit()
