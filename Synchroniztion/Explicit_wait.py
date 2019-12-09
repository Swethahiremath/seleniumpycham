from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver=webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("manager")
driver.find_element_by_id("loginButton").click()
wait=WebDriverWait(driver,3)
status=wait.until(ec.title_is("actiTIME -Enter the Time-Track"),"verifying the title")
print(status)
driver.quit()
