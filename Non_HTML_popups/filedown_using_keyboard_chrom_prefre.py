# download using keymodule method ,for this import keyboard
#keyboard.press_and_release("tab")

from selenium import webdriver
from time import sleep
import keyboard
from pathlib import Path
ffprofile=webdriver.Chrome()
filepath=
driver=webdriver.Firefox(ffprofile)
driver.get("https://selenium.dev/")

download=driver.find_elements_by_xpath("//a[text()='Downloads']")
download.click()

java_download=driver.find_elements_by_xpath("//a[text()='Java']/..//a[text()='Download']")
java_download.click()

