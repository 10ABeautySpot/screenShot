import unittest

from commonTest import CommonTest


class Close(CommonTest):
    def test_close(self):
        """close...关闭浏览器"""
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
