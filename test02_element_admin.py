import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from commonTest import CommonTest
from config.envConfig import envConfig

baseUrl = envConfig.testUrl2
username = envConfig.testUsr2
password = envConfig.testPassword2


class MyTestCase(CommonTest):
    def login(self, username, password):
        time.sleep(1)
        self.driver.maximize_window()
        usernameEle = self.driver.find_element_by_xpath('//input[@name="username"]')
        usernameEle.send_keys(Keys.CONTROL,'a')
        usernameEle.send_keys(Keys.BACKSPACE)
        usernameEle.send_keys(username)
        passwordEle = self.driver.find_element_by_xpath('//input[@name="password"]')
        passwordEle.send_keys(Keys.CONTROL,'a')
        passwordEle.send_keys(Keys.BACKSPACE)
        passwordEle.send_keys(password)
        passwordEle.send_keys(Keys.ENTER)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)
        time.sleep(3)

    def test02_001_login(self):
        """test2...登录"""
        self.redirect_URL(baseUrl + 'login')
        try:
            WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.NAME, "username")))
            self.login(username, password)
        except:
            self.assertFalse(False)


    def test02_002_document(self):
        """test2...文档"""
        self.redirect_URL(baseUrl + 'documentation/index')
        try:
            WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.XPATH, "//a[text()='国内文档']")))
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.send_error_infos('element-admin系统-文档页面')
            self.assertTrue(False)
        finally:
            self.full_print_screen(self.driver, 'element-admin系统-文档页面')

    def test02_003_icon(self):
        """test2...图标"""
        self.redirect_URL(baseUrl + 'icon/index')
        try:
            WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'icons-container')))
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.send_error_infos('element-admin系统-图标页面')
            self.assertTrue(False)
        finally:
            self.full_print_screen(self.driver, 'element-admin系统-图标页面')
        ele = self.driver.find_element_by_class_name('icons-container')

    def test02_004_theme(self):
        """test2...换肤"""
        self.redirect_URL(baseUrl + 'theme/index')
        try:
            WebDriverWait(self.driver, 60, 1).until(EC.presence_of_element_located((By.LINK_TEXT, "换肤文档")))
            self.assertTrue(True)
        except Exception as e:
            print(e)
            self.send_error_infos('element-admin系统-换肤页面')
            self.assertTrue(False)
        finally:
            self.full_print_screen(self.driver, 'element-admin系统-换肤页面')


if __name__ == '__main__':
    unittest.main()
