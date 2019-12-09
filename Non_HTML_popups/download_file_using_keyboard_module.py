from selenium import webdriver
import autoit
from time import sleep
from pathlib import Path
import keyboard
file_path=Path("C:\\Users\\SWHIRE~1.ORA\\AppData\\Local\\Temp\\selenium-java-3.141.59.zip")

driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://selenium.dev/")
download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

java_download=driver.find_element_by_xpath("//td[text()='Java']/..//a[text()='Download']").click()
sleep(3)

keyboard.press_and_release("tab")
sleep(3)

keyboard.press_and_release('enter')

sleep(20)

if file_path.is_file():
    print("File is downloaded ")
else:
    print("File is not downloaded ")
driver.close()