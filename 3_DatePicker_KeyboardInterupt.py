import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").send_keys("08/04/2020",Keys.ENTER)
time.sleep(2)
driver.quit()