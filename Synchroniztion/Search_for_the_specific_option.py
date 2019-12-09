from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
driver.get('D://Pythonpractice//seleniumpycham//Synchroniztion//Dropdown_multiple_list.html')
drop_down_ele=driver.find_element_by_name("Mobdevices")
selectmultiple=Select(drop_down_ele)
all_options=selectmultiple.options
sleep(2)
found=False
search_item="computer"
for op in all_options:
    value=opt.text
    if value==search_item:
        found=True
        break
if found:
    print("search option"+search_item+"found"+"boolen result is",found)

else:
    print("seacrh option"+search_item+" not found "+ "boolen result is ",found)