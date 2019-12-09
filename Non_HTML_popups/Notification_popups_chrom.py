from selenium import webdriver
from time import sleep

option_class= webdriver.ChromeOptions()

option_class.add_argument("--disable-notifications")

driver= webdriver.Chrome(options=option_class)
#driver= webdriver.Chrome()

driver.implicitly_wait(20)

driver.get("https://autoportal.com/newcars/hyundai/")


sleep(4)
driver.close()