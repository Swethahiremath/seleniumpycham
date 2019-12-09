#write a program to get all the window handles and close the windowhandles  one by one

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.naukri.com/")
all_windows_handles=driver.window_handles

print(all_windows_handles)

'''for handle in all_windows_handles:'''
driver.switch_to.window("Reliance Industries Limited")
driver.close()





