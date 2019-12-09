from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

#driver.find_element_by_name("sex")

#by id method with name value
#driver.find_element(By.ID,'email')

#find by using By.TAG_Name
#driver.find_element(By.TAG_NAME,'input')

#driver.find_element_by_tag_name('input')

#find element by using link text
#driver.find_element_by_link_text()
#driver.find_element(By.LINK_TEXT,'Forgotten account?')
#driver.find_element(By.LINK_TEXT,'Forgotten account?').click()
#driver.find_element_by_link_text('Forgotten account?').click()

# 4 : Find element by using Partial Link Text
#driver.find_element(By.PARTIAL_LINK_TEXT,'Forgotten').click()
#driver.find_element_by_partial_link_text('account').click()

#driver.find_element(By.ID,'email').send_keys('swetha')---- Find and send the key values
#try:
#    driver.find_element(By.ID, 'email')
#   print('Testpass')
#except Exception as e:
#    print(e)


driver.find_element_by_css_selector("input.inputtext.login_form_input_box").send_keys("swetha.hiremath@gmail.com")




time.sleep(5)
driver.close()