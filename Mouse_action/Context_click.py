from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.actimind.com")
sleep(3)
action=ActionChains(driver)
aboutcomp=driver.find_element_by_link_text("ABOUT COMPANY")
action.move_to_element(aboutcomp).context_click().perform()
sleep(2)

driver.quit()

