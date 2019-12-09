from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("D://Pythonpractice//seleniumpycham//Find_Using_Xpath//Htmlfile_for_Table.html")
time.sleep(2)

#BACKWARD
#driver.find_element_by_xpath("//table[tbody[tr[td[text()='Phyton']]]]")

#backward travercing with /..

driverd//td[text()="Phyton"]/../../..