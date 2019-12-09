from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
time.sleep(2)
driver.find_element_by_xpath("//a[@id='toPasswordRecoveryPageLink']").click()
time.sleep(3)
driver.quit()
