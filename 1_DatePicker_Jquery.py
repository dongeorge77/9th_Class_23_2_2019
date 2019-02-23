import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.implicitly_wait(30)

ele=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").click()
time.sleep(2)
driver.switch_to.parent_frame()
driver.switch_to.default_content()
driver.find_element_by_xpath("//a[text()='Draggable']").click()
time.sleep(5)
driver.quit()