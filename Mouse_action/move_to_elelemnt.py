from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.actimind.com/")
sleep(3)
action=ActionChains(driver)
areaofexp=driver.find_element_by_xpath("//a[contains(text(),'AREAS OF EXPERTISE')]")
sleep(2)
action.move_to_element(areaofexp)
action.perform()
sleep(5)
driver.quit()
