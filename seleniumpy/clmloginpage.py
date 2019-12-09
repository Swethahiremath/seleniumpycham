from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
driver=webdriver.Chrome()
driver.get("https://oalapp-crmau.oraclecorp.com/oalapp/web/clm/")

driver.maximize_window()
driver.find_element_by_id("sso_username").send_keys("swetha.hiremath@oracle.com")

driver.find_element_by_id("ssopassword").send_keys("Hmmssk$400440")
driver.find_element_by_link_text("Sign In").click()

driver.find_element_by_class_name("oj-navigationlist-focused-element oj-navigationlist-item-content")


driver.find_element_by_id("activity").click()

time.sleep(5)
driver.close()
