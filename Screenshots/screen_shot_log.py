from selenium import  webdriver
from time import  sleep

driver= webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")

logo_element=driver.find_element_by_xpath("//div[@class='atLogoImg']")


location =logo_element.location
logo_size=logo_element.size

x=location['x']
y=logo_element['y']

width=location[x]+logo_size['width']
height=location[y]+logo_size['height']

im=Image.open("C:\\loginpage.png")

