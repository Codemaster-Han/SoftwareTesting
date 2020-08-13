# 将所有的自动化测试功能放在一个.py文件中，方便使用unittest测试框架批量执行

import time
import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestChrom01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    #   登录测试
    def test_01(self):
        self.driver.get("http://localhost:8080/ses/public/index.html")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 先定位到用户名和密码的输入框，点击登录
        # driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("abc")
        time.sleep(2)
        driver.find_element_by_name("password").send_keys("123")
        time.sleep(2)
        # 通过定位密码框，回车enter来代替click()
        driver.find_element_by_id("btn_login").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.quit()

    # 新增记录测试
    def test_02(self):
        self.driver.get("http://localhost:8080/ses/public/index.html")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 先定位到用户名和密码的输入框，点击登录
        driver.find_element_by_name("username").send_keys("abc")
        driver.find_element_by_name("password").send_keys("123")
        time.sleep(2)

        # 通过定位密码框，回车enter来代替click()
        driver.find_element_by_id("btn_login").send_keys(Keys.ENTER)
        time.sleep(5)

        # # 定位弹出框，并点击关闭
        # driver.find_element(By.CSS_SELECTOR, "#main_fail_modal_dialog span").click()
        # xpath定位，这个等号后面必须是单引号，而从网页直接复制过来的双引号，需要修改
        driver.find_element_by_xpath("//*[@id='main_fail_modal_dialog']/div/div[3]/button").click()
        driver.implicitly_wait(10)

        # 点击成绩管理
        driver.find_element_by_link_text("成绩管理").click()
        driver.implicitly_wait(10)
        # 点击新增按钮，点击下拉框选择
        driver.find_element_by_id("exam_record_table_toolbar_add").click()
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_add_form']/div[1]/div/button").click()
        driver.find_element_by_xpath(
            "//*[@id='exam_record_table_toolbar_add_modal']/div[2]/div/div[2]/ul/li[1]/a/span[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_add_form']/div[2]/div/button").click()
        driver.find_element_by_xpath(
            "//*[@id='exam_record_table_toolbar_add_modal']/div[2]/div/div[2]/ul/li[1]/a/span[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_add_form_score']").send_keys("55")
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_add_form_submit']").click()
        time.sleep(3)

        driver.quit()

    # 查询考试成绩记录
    def test_03(self):
        self.driver.get("http://localhost:8080/ses/public/index.html")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 先定位到用户名和密码的输入框，点击登录
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
        driver.implicitly_wait(3)
        # 定位搜索框，输入要查询的id'
        driver.find_element_by_xpath("//*[@id='exam_record_panel']/div[1]/div[1]/div[3]/input").send_keys("2")
        time.sleep(2)
        # 按下回车键
        driver.find_element_by_xpath("//*[@id='exam_record_panel']/div[1]/div[1]/div[3]/input").send_keys(Keys.ENTER)
        time.sleep(5)
        driver.quit()

    # 删除考试记录
    def test_04(self):
        self.driver.get("http://localhost:8080/ses/public/index.html")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 先定位到用户名和密码的输入框，点击登录
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
        # 勾选删除的考试记录
        driver.find_element_by_xpath("//*[@id='exam_record_table']/tbody/tr[2]/td[1]/label/input").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='exam_record_table']/tbody/tr[3]/td[1]/label/input").click()
        time.sleep(2)
        # 点击删除,点击提交
        driver.find_element_by_id("exam_record_table_toolbar_delete").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_delete_confirm_modal_submit']").click()
        time.sleep(2)
        driver.quit()

     # 修改考试记录
    def test_05(self):
        self.driver.get("http://localhost:8080/ses/public/index.html")
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 先定位到用户名和密码的输入框，点击登录
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
        driver.find_element_by_xpath(
            "//*[@id='exam_record_table_toolbar_update_modal']/div[2]/div/div[2]/ul/li[2]/a/span[2]").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath("//*[@id='exam_record_table_toolbar_update_form']/div[2]/div/button").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(
            "//*[@id='exam_record_table_toolbar_update_modal']/div[2]/div/div[2]/ul/li[2]/a/span[2]").click()
        time.sleep(2)
        driver.find_element_by_id("exam_record_table_toolbar_update_form_submit").click()
        time.sleep(2)
        try:
            print("==================")
            print(driver.title)
            self.assertEqual(u"12345上网从这里开始", driver.title)
        except:
            self.saveScreenShot(driver, "错误截图.png")
            time.sleep(3)
            driver.quit()

    # 截图创建
    def saveScreenShot(self, driver, file_name):
        if not os.path.exists("./errorImageFile"):
            os.makedirs("./errorImageFile")
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        print(now)
        driver.get_screenshot_as_file("./errorImageFile/" + now + "-" + file_name)  # 截图命名并保存
        time.sleep(3)