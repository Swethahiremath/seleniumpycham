from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.google.com")
sleep(2)
search_box=driver.find_element_by_name('q')
sleep(2)
search_box.send_keys('Python')
sleep(2)

# Search all the elements form the suggersion using find elements and find the lenght
all_options=driver.find_elements_by_xpath("//ul[@role='listbox']/li")
print(len(all_options))

#print the all the suggeresions
for option in all_options:
    print(option.text)

#find the 6th element and print
sixth_auto_suggestion=all_options[5]
print("The six suggesion is ",sixth_auto_suggestion.text)
sixth_auto_suggestion.click()
driver.quit()



