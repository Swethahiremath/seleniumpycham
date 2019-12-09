from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("D://Pythonpractice//seleniumpycham//Find_Using_Xpath//Listpage.html")
time.sleep(2)
#Find the element with Axes forward following func
#driver.find_element_by_xpath("//li[contains(text(),'Delhi')]/following::li")

#Find the element with Axes backward preceding func
#driver.find_element_by_xpath("//li[contains(text(),'Chennai')]/preceding::li")

#Find the element with Axes child function
#driver.find_element_by_xpath("//ul[@id='orderparent']/child::ul")

#Find the element with Axes parent function
driver.find_element_by_xpath("//ul[@id='parent']//parent::ul")
or
//li[contains(text(),'Chennai')]//parent::ul

#Find the element with Axes ancestor function
driver.find_element_by_xpath("//li[contains(text(),'HSR')]//ancestor::ul")

#Find the element with Axes descendant function
driver.find_element_by_xpath("//ul[@id='orderparent']//descendant::li")



time.sleep(4)
driver.close()