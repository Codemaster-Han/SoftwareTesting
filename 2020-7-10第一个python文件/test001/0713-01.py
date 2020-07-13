from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("新冠肺炎")
driver.implicitly_wait(5)
driver.find_element_by_id("su").click()
driver.maximize_window()

driver.find_element_by_link_text(u"新冠肺炎疫情分布").click()
driver.implicitly_wait(5)
driver.set_window_size(400, 400)
time.sleep(10)
title1 = driver.title
print("title"+title1)

driver.quit()