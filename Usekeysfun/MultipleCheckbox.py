from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
un = driver.find_element_by_id('username')
un.send_keys('admin')
pw=driver.find_element_by_name('pwd')
pw.send_keys('manager')
login=driver.find_element_by_xpath("//a[@id='loginButton']")
login.send_keys(Keys.ENTER)
sleep(5)
task = driver.find_element_by_xpath("//a[@class='content tasks']")
task.send_keys(Keys.ENTER)
sleep(3)

row1=driver.find_element_by_xpath("//div[text()='Bug fixing'])[1]/parent::div/parent::div/parent::div/parent::td/preceding-sibling::td/div")
sleep(1)
valuerow1=row1.get_attribute('class')
print(valuerow1)

if 'inactive' in valuerow1:
    row1.click()

sleep(2)



