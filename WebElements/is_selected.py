from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
link=driver.find_element_by_xpath("//input[@id='keepLoggedInCheckBox']")
sleep(2)
link.click()
if link.is_selected():
    print('element is selected ')
else:
    print('element is not selected ')

driver.quit()