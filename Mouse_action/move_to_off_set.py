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
#action.move_to_element(areaofexp)
#move_to_offset
locationofelm=areaofexp.location
x=locationofelm.get('x')
y=locationofelm.get('y')
sleep(3)
action.move_by_offset(x,y).perform()

sleep(5)
driver.quit()
