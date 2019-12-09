from selenium import webdriver
import autoit
from time import sleep
from pathlib import Path
file_path=Path("C:\\Users\\SWHIRE1.ORA\\AppData\\Local\\Temp\\selenium-java-3.141.59.zip")
#file_path=Path("D:\\selenium-java-3.141.59.zip")

driver=webdriver.Firefox()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get("https://selenium.dev/")
download = driver.find_element_by_xpath("//a[text()='Downloads']")
download.click()

java_download=driver.find_element_by_xpath("//td[text()='Java']/..//a[text()='Download']").click()
sleep(3)
autoit.win_wait_active("Opening selenium-java-3.141.59.zip",6)
sleep(3)

autoit.send("{TAB}")
autoit.send("{ENTER}")

sleep(5)

if file_path.is_file():
    print("File is downloaded ")
else:
    print("File is not downloaded ")
driver.close()