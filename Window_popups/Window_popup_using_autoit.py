from selenium import webdriver
import autoit
from time import sleep
from pathlib import Path

driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://selenium.dev/")
driver.implicitly_wait(3)

download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

driver.find_element_by_xpath("//a[text()='3.141.59']").click()

autoit.win_wait_active("Opening selenium-server-standalone-3.141.59.jar",4)
sleep(3)
autoit.send("{LEFT}")
autoit.send("{ENTER}")
sleep(4)
driver.close()