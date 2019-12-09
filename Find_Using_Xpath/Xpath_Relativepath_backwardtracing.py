from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.seleniumhq.org/")
time.sleep(2)
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Download']").click()
time.sleep(3)
#driver.find_element_by_xpath("//table[tbody[tr[td[text()='Python']]]]").text
driver.find_element_by_xpath("//a[text()='Opera']").click()
#driver.find_element_by_xpath("//table[tbody[tr[td[a[text()='Opera']]]]]").click()
time.sleep(10)
driver.close()