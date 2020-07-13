from selenium import webdriver
import time

drive = webdriver.Chrome()
drive.get("http://www.baidu.com")

drive.find_element_by_id("kw").send_keys("张东升")
drive.find_element_by_id("su").submit()
drive.maximize_window()
time.sleep(5)
drive.back()
time.sleep(5)
drive.forward()

time.sleep(3)
drive.quit()