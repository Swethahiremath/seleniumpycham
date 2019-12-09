from selenium import webdriver
from time import sleep
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webnotifications.enabled",False)
driver = webdriver.Firefox(profile)
driver.implicitly_wait(50)
#driver.get("https://www.uber.com/in/en/")
driver.get("https://autoportal.com/newcars/hyundai/")
driver.maximize_window()
sleep(3)
#ride1=driver.find_element_by_xpath("//span[@class='bw ct cu sn hi c4 ck cl so sp sq'][contains(text(),'Ride')]")
#ride1.click()
driver.close()

#locate=driver.find_element_by_xpath("//div[@class='an re xr cj bf dr bw c4 hi']").click()








