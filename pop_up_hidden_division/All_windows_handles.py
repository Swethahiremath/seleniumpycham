from selenium import webdriver

driver=webdriver.Chrome()

driver.get("https://selenium.dev/")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element_by_xpath("//a[text()='Downloads']").click()
all_window_handles=driver.window_handles
for handle in all_window_handles:
    print("Current window handle",handle)
driver.close()


