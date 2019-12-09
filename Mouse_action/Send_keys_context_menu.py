from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.actimind.com")
sleep(3)
action=ActionChains(driver)
aboutcomp=driver.find_element_by_link_text("ABOUT COMPANY")
action.move_to_element(aboutcomp).context_click().perform()
sleep(1)
#aboutcomp.send_keys(Keys.CONTROL+Keys.ENTER)

aboutcomp.send_keys(Keys.SHIFT+Keys.ENTER)


sleep(2)
driver.quit()

