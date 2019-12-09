from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.craftsvilla.com")
time.sleep(2)
driver.maximize_window()
driver.find_element_by_xpath("//*[text()='SAREES']").click()
time.sleep(3)
#driver.find_element_by_xpath("//table[tbody[tr[td[text()='Python']]]]").text
driver.find_element_by_xpath("//*[text()=\"Women's fashion\"]").click()
#driver.find_element_by_xpath("//table[tbody[tr[td[a[text()='Opera']]]]]").click()
time.sleep(5)
driver.close()

