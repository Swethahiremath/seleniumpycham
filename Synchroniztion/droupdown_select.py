from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
driver.get('D://Pythonpractice//seleniumpycham//Synchroniztion//dropdown_list_thml.html')
drop_down_ele=driver.find_element_by_name("dropdown")
select=Select(drop_down_ele)
sleep(2)
#selecct dropdown element by index
#select.select_by_index(2)

#2) Select element by using value
#select.select_by_value('Py')

#3) Select element by visible text
#select.select_by_visible_text('Python')

#4) to identify the select option is with single or multiple select list box
'''if select.is_multiple:
    print('List box is multi select list box')
else:
    print('List box is single select list box')  '''

#5) To count the number of options in the list box
count_option=select.options
print('Total number of options present in the list box count option',len(count_option))

for op in count_option:
    print(op.text)



sleep(3)
driver.close()
