from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.istqb.in")
sleep(3)
action=ActionChains(driver)
foundation=driver.find_element_by_xpath("//a[text()='FOUNDATION'][1]")
action.move_to_element(foundation).perform()

sleep(2)
onlineelement=driver.find_element_by_xpath("//a[text()='ONLINE ENROLLMENT'][1]")
action.move_to_element(onlineelement).pause(5)
print("Its Paused ")

action.click(onlineelement).perform()

print("Its Clicked")
