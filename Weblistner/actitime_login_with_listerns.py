from selenium import webdriver
from time import sleep
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from Weblistner.listener import MyListeners

driver=webdriver.Chrome()
event_driver=EventFiringWebDriver(driver,MyListeners())
event_driver.implicitly_wait(10)
event_driver.get("https://demo.actitime.com/login.do")





