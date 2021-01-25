# 字典对应：
# | test 1 | 百度网页           |
# | test 2 | elementui-admin  |
import time
import unittest

suite1 = unittest.TestSuite()
suite2 = unittest.TestSuite()
suiteClose = unittest.TestSuite()


def start():
    with open('report/result.txt', 'a', encoding='utf-8') as file:
        file.truncate(0)
    # load tests to suite1
    suite1.addTests(unittest.defaultTestLoader.discover('./', pattern='test01*.py'))
    # load tests to suite2
    suite2.addTests(unittest.defaultTestLoader.discover('./', pattern='test02*.py'))
    # 关闭浏览器
    suiteClose.addTests(unittest.defaultTestLoader.discover('./', pattern='test_999_close.py'))

def runTestSuite(suite, description):
    time.sleep(2)
    with open('report/result.txt', 'a', encoding='utf-8') as file:
        runner = unittest.TextTestRunner(stream=file, descriptions=description, verbosity=2)
        runner.run(suite)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

    # run test1
    runTestSuite(suite1, "test1 百度网页")

    # run test2
    runTestSuite(suite2, "test2 element-admin")

    # close window
    runTestSuite(suiteClose, "关闭窗口")
