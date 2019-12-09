# download using keymodule method ,for this import keyboard
#keyboard.press_and_release("tab")

from selenium import webdriver
from time import sleep
import keyboard
from pathlib import Path
ffprofile=webdriver.FirefoxProfile()
ffprofile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/zip")
#download in desktop
ffprofile.set_preference("browser.download.folderList",0)
#download in specified folder
ffprofile.set_preference("browser.download.folderList",2)
ffprofile.set_preference("browser.download.dir","D:\\")
driver=webdriver.Firefox(ffprofile)
driver.get("https://selenium.dev/")
driver.implicitly_wait(3)

download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

sleep(3)
java_download=driver.find_element_by_xpath("//td[text()='Java']/..//a[text()='Download']")
java_download.click()





