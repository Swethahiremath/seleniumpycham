from selenium import webdriver
from time import sleep

download_path=("D:\\")

Chromepref={"profile.default_content_settings.popups":0,
            "download.default_directory":download_path,
            "safebrowsing.enabled":True}

options=webdriver.ChromeOptions()
options.add_experimental_option("prefs",Chromepref)

driver=webdriver.Chrome(options=options)
driver.get("https://selenium.dev/downloads")

driver.implicitly_wait(20)
driver.maximize_window()

dwonload_link=driver.find_element_by_xpath("//a[text()='3.141.59']").click()

sleep(7)
