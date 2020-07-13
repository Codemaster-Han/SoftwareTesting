from selenium import webdriver
import time

driver = webdriver.Chrome()    #记得是有括号的（）
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("乃万")
driver.find_element_by_id("su").click()
title01 = driver.title
print("title1"+title01)
driver.implicitly_wait(10)
driver.find_element_by_link_text(u"乃万_百度百科").click()
title02 = driver.title
print("title2"+title02)
url = driver.current_url
print(url)


time.sleep(5)
driver.quit()