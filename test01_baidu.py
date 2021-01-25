import unittest
from commonTest import CommonTest
from config.envConfig import envConfig

baseUrl = envConfig.testUrl1


class MyTestCase(CommonTest):
    def test01_1_home(self):
        """test1...打开百度首页"""
        try:
            self.redirect_URL(baseUrl)
        except:
           self.send_error_infos('百度-首页')
        finally:
            self.full_print_screen(self.driver, '百度-首页')


if __name__ == '__main__':
    unittest.main()
