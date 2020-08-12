from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8080/ses/public/index.html")

driver.maximize_window()
driver.implicitly_wait(30)
#先定位到用户名和密码的输入框，点击登录
driver.find_element_by_name("username").send_keys("abc")
driver.find_element_by_name("password").send_keys("123")
time.sleep(2)

# 通过定位密码框，回车enter来代替click()
driver.find_element_by_id("btn_login").send_keys(Keys.ENTER)
time.sleep(2)

# # 定位弹出框，并点击关闭
# driver.find_element(By.CSS_SELECTOR, "#main_fail_modal_dialog span").click()
# xpath定位，这个等号后面必须是单引号，而从网页直接复制过来的双引号，需要修改
driver.find_element_by_xpath("//*[@id='main_fail_modal_dialog']/div/div[3]/button").click()
driver.implicitly_wait(10)

# 点击成绩管理
driver.find_element_by_link_text("成绩管理").click()
# 勾选一个考试信息记录，点击修改按钮
driver.find_element_by_xpath("//*[@id='exam_record_table']/tbody/tr[2]/td[1]/label/input").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update']").click()
time.sleep(2)
# 选择需要修改的信息
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update_form']/div[1]/div/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update_modal']/div[2]/div/div[2]/ul/li[2]/a/span[2]").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update_form']/div[2]/div/button").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update_modal']/div[2]/div/div[2]/ul/li[2]/a/span[2]").click()
time.sleep(2)
driver.find_element_by_id("exam_record_table_toolbar_update_form_submit").click()
time.sleep(2)
driver.quit()