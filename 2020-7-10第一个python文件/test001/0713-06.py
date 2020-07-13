#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("创造营303")
su1=driver.find_element_by_id("su")
time.sleep(3)
ActionChains(driver).context_click(su1).perform() #右键
ActionChains(driver).double_click(su1).perform() #双击

#三个单引号是多行注释
'''
#定位元素的原位置
element = driver.find_element_by_id("s_is_result_css")
#定位元素要移动到的目标位置
target = driver.find_element_by_class_name("btn")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element, target).perform()
'''
time.sleep(3)
driver.quit()