from selenium import webdriver
#from selenium.webdriver.common import by
import time
driver=webdriver.Chrome()
driver.get("D://Pythonpractice//seleniumpycham//Find_Using_Xpath//Html_usin_div.html")
time.sleep(2)

#xpath to identify individual elements
#driver.find_element_by_xpath("/html/body/div[1]/input[1]").send_keys("Swetha")

#xpath to identify ab and cd
#driver.find_element_by_xpath("/html/body/div[1]/input")

#xpath to identify ca and bd
#driver.find_element_by_xpath("/html/body/div/input[1]")
#driver.find_element_by_xpath("/html/body/div/input[2]")

#xpath to identify abcd
#driver.find_element_by_xpath("/html/body/div/input")

#xpatch to identify AD which are in different position
driver.find_element_by_xpath("/html/body/div[1]/input[1] | /html/body/div[2]/input[2]")
driver.find_element_by_xpath("/html/body/div[1]/input[2] | /html/body/div[2]/input[1]")
driver.find_element_by_xpath("/html/body/div[1]/input | /html/body/div[2]/input[1])

time.sleep(4)
driver.close()