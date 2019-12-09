from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
driver.get('D://Pythonpractice//seleniumpycham//Synchroniztion//Dropdown_multiple_list.html')
drop_down_ele=driver.find_element_by_name("Mobdevices")
selectmultiple=Select(drop_down_ele)
all_options=selectmultiple.options
sleep(2)
all_items=[]
for op in all_options:
    value=op.text
    all_items.append(value)

all_items.sort()
sleep(2)
for v in all_items:
    print(v)
    sleep(2)
driver.quit()
