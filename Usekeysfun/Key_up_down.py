from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from time import sleep
driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")
link=driver.find_element_by_xpath("//select[@id='day']")
link.send_keys(Keys.ENTER)
link.send_keys('Day')
for i in range(3):
    sleep(3)
    link.send_keys(Keys.ARROW_DOWN)
link.send_keys(Keys.ENTER)

month=driver.find_element_by_xpath("//select[@id='month']")
month.send_keys(Keys.ENTER)
month.send_keys('Month')
for i in range(11):
    sleep(1)
    month.send_keys(Keys.ARROW_DOWN)
month.send_keys(Keys.ENTER)

#actions.move_to_element(link).context_click().send_keys(Keys.COMMAND+'t').perform()
#link.send_keys(Keys.CONTROL+Keys.ENTER)

sleep(4)
driver.quit()
