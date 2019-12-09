from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.seleniumhq.org/")
sleep(2)
driver.implicitly_wait(20)

driver.find_element_by_xpath("//li[@id='menu_download']/a").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Javadoc')]").click()
sleep(2)
#find frames by name
#driver.switch_to.frame("classFrame")

#find frames by index
driver.switch_to.frame(1)

#find frames by webelemets
#frameobject=driver.find_element(By.XPATH,"//frame[@name='classFrame']")
#driver.switch_to.frame(frameobject)
#sleep(1)
#driver.find_element(By.XPATH,"//a[contains(text(),'Frames')][1]").click()
driver.find_element(By.XPATH,"//a[contains(text(),'AbstractAnnotations')]").click()
sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")

#frame2win=driver.find_element(By.XPATH,"//frame[@name='classFrame']")

#driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html?overview-summary.html")
#driver.refresh()

driver.find_element(By.XPATH,"//dd/a[contains(text(),'Annotations')]").click()
print("Success")
sleep(10)
driver.switch_to.default_content()


sleep(5)
driver.quit()
