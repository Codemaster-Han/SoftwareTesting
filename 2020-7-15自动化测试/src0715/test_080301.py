# Generated by Selenium IDE
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test080301(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(932, 659)
        self.driver.find_element(By.ID, "kw").send_keys("乘风破浪的姐姐")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(2)