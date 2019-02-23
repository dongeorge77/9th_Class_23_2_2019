import os
import time

from selenium import webdriver

proj_path=os.getcwd()
driver_path=proj_path.replace("\\","/")+"/Driver"
print(driver_path)
driver=webdriver.Chrome(executable_path=driver_path+"/chromedriver.exe")
driver.get("http://facebook.com")
driver.maximize_window()
time.sleep(3)
driver.quit()