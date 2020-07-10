from selenium import webdriver
import time

driver=webdriver.Chrome();
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_link_text("新闻").click()
time.sleep(6)
driver.quit()

