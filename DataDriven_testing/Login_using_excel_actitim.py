from selenium.common.exceptions import   TimeoutExceptions
from selenium.webdriver.support.wait import  import WebDriverWait
from selenium.webdriver.support import expeccted_conditions as ec

def login(un,pwd,expected_result):
     driver=webdriver.Chrome()
     driver.maximize_window()
     driver.get("https://demo.actitime.com/login.do")
     driver.find_element_by_id("username").send_keys(un)
     driver.find_element_by_id("pwd").send_keys(pwd)
     driver.find_element_by_id("loginButton").click()



    wait = WebDriverWait(driver,10)
    status=False
    try:
        status=wait.until(ec.title_is(expected_result))
    except TimeoutExceptions:
        status

    return status
    
