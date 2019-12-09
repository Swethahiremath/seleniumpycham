from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
driver.get('D://Pythonpractice//seleniumpycham//Synchroniztion//Dropdown_multiple_list.html')
drop_down_ele=driver.find_element_by_name("Mobdevices")
selectmultiple=Select(drop_down_ele)
'''all_options=selectmultiple.options
sleep(2)

for op in all_options:
    selectmultiple.select_by_visible_text(op.text)

sleep(2)

selectmultiple.deselect_all()
sleep(2)'''

#Select the first option from the selct
first_selec_opt=selectmultiple.first_selected_option
print('First selected option',first_selec_opt.text)
sleep(3)

# Write a script to select  the option and deselct by index ,value ,visible text
#Write a script to get all the options

driver.quit()