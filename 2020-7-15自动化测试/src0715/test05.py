#
#功能：实现DDT数据驱动
#
import unittest
import sys, csv
import time
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By

#读取Txt文件的方法
def getCsv(file_name):
    rows = []
    path = sys.path[0]

    with open(path+'/data/'+file_name, mode='rt', encoding='utf-8') as f:
        readers = csv.reader(f, delimiter=',', quotechar='|')
        next(readers, None)
        for row in readers:
            temprows=[]
            for i in row:
                temprows.append(i)
            rows.append(temprows)
        return rows

@ddt
class Baidu1(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(30)
            self.base_url="http://www.baidu.com"
            self.driver.maximize_window()
            self.verificationErrors = []
            self.accept_next_alert = True
        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)

        # @unpack
        # @file_data('test_baidu_data.json')
        # 输入几个参数，就执行几次方法
        # 用数据的个数去驱动方法运行的次数，就是数据驱动

        # 第1种用法
        @unittest.skip("skipping")
        @data("王凯", "虞书欣", "刘雨欣", "赵小棠", "上官喜爱")
        def test_baidu1(self, value):
            driver = self.driver
            driver.get(self.base_url + "/")
            driver.maximize_window()
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(value)
            driver.find_element_by_id("su").click()
            time.sleep(5)

        # 第2种用法
        @data(*getCsv('test_baidu_data.txt'))
        @unpack
        def test_baidu2(self, value, expected_value):
            driver = self.driver
            driver.get(self.base_url + "/")
            driver.maximize_window()
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(value)
            driver.find_element_by_id("su").click()
            time.sleep(5)
            self.assertEqual(expected_value, driver.title, msg="搜索结果与期待值不一样")
            time.sleep(3)


        # 第3种用法
        @unittest.skip("skipping")
        @data([u"王凯", u"王凯_百度搜索"], [u"虞书欣", u"虞书欣_百度搜索"],  ["赵小棠", u"大鱼海棠_百度搜索"])
        @unpack
        def test_baidu3(self, value, expected_value):
            driver = self.driver
            driver.get(self.base_url + "/")
            driver.maximize_window()
            driver.find_element_by_id("kw").clear()
            driver.find_element_by_id("kw").send_keys(value)
            driver.find_element_by_id("su").click()
            time.sleep(5)
            self.assertEqual(expected_value, driver.title, msg="搜索结果与期待值不一样")
            print(expected_value)
            print(driver.title)

if __name__ == "__main__":
    unittest.main()