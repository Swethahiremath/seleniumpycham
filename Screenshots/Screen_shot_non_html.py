from selenium import  webdriver
from time import sleep
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()


driver.get("D:\File_upload_ex.html")
browser=driver.find_element_by_name("file1").click()
#sleep(2)
#browser.click()
driver.get_screenshot_as_file("fileupload.png")

driver.close()


