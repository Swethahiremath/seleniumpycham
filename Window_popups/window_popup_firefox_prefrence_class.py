
from selenium import webdriver
from time import sleep
import keyboard
from pathlib import Path
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/java-archive")
driver=webdriver.Firefox(profile)
driver.implicitly_wait(20)
driver.get("https://selenium.dev/")
driver.maximize_window()


download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

driver.find_element_by_xpath("//a[text()='3.141.59']").click()

sleep(5)
driver.close()



