#coding=utf-8
from selenium import webdriver
import time
#访问百度
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.maximize_window()
#搜索
driver.find_element_by_id("kw").send_keys("虞书欣")
driver.find_element_by_id("su").click()
time.sleep(3)
#控制页面滚动条拖到_底部
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#控制滚动条移动到页面的_顶部
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

#同时控制滚动条的左右，上下
driver.set_window_size(400, 500)
time.sleep(3)
js = "window.scrollTo(200,200)"
driver.execute_script(js)
time.sleep(4)

driver.quit()