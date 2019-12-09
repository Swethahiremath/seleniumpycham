from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
un = driver.find_element_by_id('username')
un.send_keys('admin')
pw=driver.find_element_by_name('pwd')
pw.send_keys('manager')
coutno = un.get_attribute('value')
n=len(coutno)
print(n)
#un.send_keys(n*Keys.BACK_SPACE)
for i in range(0,n+1):
    if i<=n:
        un.send_keys(Keys.BACKSPACE)
        sleep(2)
un.send_keys("trainee")
pw.clear()
pw.send_keys("trainee")
login=driver.find_element_by_xpath("//a[@id='loginButton']").send_keys(Keys.ENTER)
sleep(3)
driver.quit()



