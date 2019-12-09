from selenium import webdriver
import autoit
from time import sleep
from pathlib import Path
import keyboard

driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://selenium.dev/")
driver.implicitly_wait(3)

download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

driver.find_element_by_xpath("//a[text()='3.141.59']").click()
sleep(2)
keyboard.press_and_release("LEFT")
sleep(2)
keyboard.press_and_release("ENTER")
sleep(5)
driver.close()