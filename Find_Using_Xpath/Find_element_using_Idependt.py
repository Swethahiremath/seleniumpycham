from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("https://www.seleniumhq.org/")
time.sleep(2)

driver.find_element_by_xpath("//a[text()='Download']").click()
time.sleep(2)
#find element using idependednt elemnt and locate the child
driver.find_element_by_xpath("//td[text()='Ruby']/../td[4]/a")

#driver.find_element_by_xpath("//td[text()='Python']/../td[4]/a")
time.sleep(3)
driver.close()