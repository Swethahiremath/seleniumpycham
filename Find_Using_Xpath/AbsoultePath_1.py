from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("D://Pythonpractice//seleniumpycham//Find_Using_Xpath//Sametags.html")
time.sleep(2)

driver.find_element_by_xpath("/html/body/input[1]").send_keys("Swetha")
driver.find_element_by_xpath("/html/body/input[2]").send_keys("Password")
time.sleep(4)
driver.close()