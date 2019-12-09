from selenium import webdriver
import pyautogui

driver= webdriver.Chrome()

driver.implicitly_wait(20)
driver.maximize_window()

driver.get("D:\File_upload_ex.html")")