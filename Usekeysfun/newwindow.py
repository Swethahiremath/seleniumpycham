from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
driver=webdriver.Chrome()
#actions=ActionChains(driver)
driver.get("https://www.google.co.in/")
link=driver.find_element_by_xpath("//a[text()='Gmail']")
#link.click()
#actions.move_to_element(link).context_click().send_keys(Keys.COMMAND+'t').perform()
link.send_keys(Keys.SHIFT,Keys.ENTER)








