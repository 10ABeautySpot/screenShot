import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.localhostConfig import localhostConfig
from config.envConfig import envConfig
from WorkWeixinRobot.work_weixin_robot import WWXRobot
from selenium.webdriver.firefox.options import Options

exportUrl = localhostConfig.exportUrl
wwx = WWXRobot(key=envConfig.wwxKey)


class CommonTest(unittest.TestCase):
    firefox_options = Options()
    firefox_options.set_preference("browser.download.dir", exportUrl)  #设置文件导出地址
    firefox_options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
    firefox_options.add_argument('--kiosk')  # 全屏 类似F11
    firefox_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    firefox_options.add_argument('--incognito')  # 隐身模式（无痕模式）
    firefox_options.add_argument('--headless')  # 浏览器不提供可视化页面
    # 创建浏览器对象
    dr = webdriver.Firefox(options=firefox_options)

    @classmethod
    def setUpClass(cls, driver=dr) -> None:
        cls.driver = driver

    def redirect_URL(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        time.sleep(5)

    def send_error_infos (self, title):
        """
        发送错误消息
        """
        wwx.send_markdown(content="<font color=\"warning\">【" + title + "】打开界面失败</font>")

    def full_print_screen(self, driver, title):
        """
        全屏截图，截取整个当前web界面，保存到指定路径
        :return: 返回文件路径+名称
        """
        try:
            current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 格式化时间
            image_url = exportUrl + '/' + current_time + ".png"  # 组合路径与名称
            driver.get_screenshot_as_file(image_url)  # 截图
            wwx.send_image(local_file=image_url)
            wwx.send_text(content=title)
            return image_url
        except Exception as e:
            print(e)
            wwx.send_markdown(content="<font color=\"warning\">【" + title + "】截图失败</font>")

    @classmethod
    def tearDownClass(cls, driver=dr) -> None:
        time.sleep(2)
