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

driver.switch_to.frame("classFrame")
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Frames')][1]")
print("clicked on Frames")

driver.switch_to.default_content()


driver.switch_to.frame("packageListFrame")

print("Control in frame one Pakages")

driver.find_element_by_link_text("com.thoughtworks.selenium").click()

sleep(5)
driver.quit()