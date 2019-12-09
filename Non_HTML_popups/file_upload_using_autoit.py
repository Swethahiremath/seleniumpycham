from selenium import webdriver
from time import sleep
import autoit
driver = webdriver.Chrome()

driver.implicitly_wait(20)

driver.maximize_window()

driver.get("D:\\Pythonpractice\\seleniumpycham\\File_upload_ex.html")
sleep(3)
driver.find_element_by_name("file1").click()

#assert isinstance(browser.click, object)


sleep(5)
path="D:\\Pythonpractice\\seleniumpycham\\pop_up_hidden_division\\child_popups.py"

autoit.win_wait_active("Open",6)
sleep(3)

autoit.control_set_text("Open","Edit1",path)
sleep(3)

autoit.control_click("Open","Button1")

sleep(3)

driver.close()