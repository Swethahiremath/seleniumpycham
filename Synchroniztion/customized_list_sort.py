from time import sleep

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.yatra.com/")
sleep(2)

depart_text_box=driver.find_element_by_xpath("//input[@name='flight_origin'][@type='text'][@id='BE_flight_origin_city']")
sleep(2)
depart_text_box.clear()
sleep(2)
depart_text_box.click()

depart_text_box.send_keys("BOM")
sleep(2)

list_all_autosugg=driver.find_elements_by_xpath("//ul/div[@class='viewport']/div/div/li")
print("List of autosuggersion ",list_all_autosugg.text)

#sleep(5)

#driver.quit()


