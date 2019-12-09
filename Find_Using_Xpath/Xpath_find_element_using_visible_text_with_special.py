from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.maximize_window()
#driver.find_element_by_xpath("//*[text()=\"Today's Deals\"]").click()

driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']").send_keys('toys')
driver.find_element_by_xpath("//div[@class='nav-search-submit nav-sprite']").click()
#driver.find_element_by_xpath("//i[@aria-label='Prime Eligible']/../div/label/input[@type='checkbox'][1]").click()
driver.find_element_by_xpath("//i[@class='a-icon a-icon-checkbox'][1]").click()

driver.find_element_by_xpath("")


time.sleep(3)

driver.close()

