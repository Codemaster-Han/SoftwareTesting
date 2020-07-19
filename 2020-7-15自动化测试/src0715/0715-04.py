'''
下拉框定位
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
driver= webdriver.Chrome()
#先打开自己的html
file_path = 'file:///' + os.path.abspath('D:\\java\\drop_down.html')
driver.get(file_path)
time.sleep(2)
#先定位到下拉框
m=driver.find_element_by_id("ShippingMethod")
#再点击下拉框下的选项
#通过xpath定位
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
#通过定位一组元素
list = driver.find_element_by_tag_name("option")
#通过循环定位
for list in lists:
    if list.get_attribute('value')=="10.69";
       list.click()
time.sleep(6)
#通过数组下标定位
lists[5].click()
time.sleep(5)

driver.quit()