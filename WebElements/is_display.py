from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
link=driver.find_element_by_link_text("Forgot your password?")
sleep(2)
if link.is_displayed():
    print('Link text is displayed ')
else:
    print('Link text is not displayed ')

driver.quit()
