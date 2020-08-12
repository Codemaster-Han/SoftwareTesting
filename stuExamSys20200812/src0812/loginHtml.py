#coding = utf-8
from selenium import webdriver
import time
import ddt
import os, sys, csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
#先打开自己的html
file_path = 'file:///' + os.path.abspath('D:\\Java\\2_codeme\\javaProject\\Java14\\stu-exam-sys\\src\\main\\webapp\\public\\index.html')
driver.get(file_path)
driver.maximize_window()
driver.implicitly_wait(30)
#先定位到用户名和密码的输入框，点击登录
# driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("abc")
time.sleep(2)
driver.find_element_by_name("password").send_keys("123")
time.sleep(2)
# 通过定位密码框，回车enter来代替click()
driver.find_element_by_id("btn_login").send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()