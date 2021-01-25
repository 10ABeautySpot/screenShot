# screenShot
**_环境：_** python3 + selenium3 + webdriver

**_依赖：_** 

selenium

urllib3

WorkWeixinRobot

xlrd  ===          注意使用版本 1.2.0



**_目录说明_**

|-—config

| ----envConfig   环境地址变量配置文件，主要用来存放网页地址，账号，密码等信息

| ----localhostConfig  本地环境地址变量配置文件，主要用来存放文件下载地址

|——report

|————result.txt   每一次执行后的结果，可利用该文件做一些可视化页面

|——commonTest  公用方法

|——main.bat  执行main.py的批处理文件，用来做计划任务

|——deleteImage.bat  执行删除生成的图片文件的批处理文件，用来做计划任务

|——main.py  执行入口

|——test_0x_xxx.py   测试用例

|——test_999_close.py  关闭浏览器


**_用法：_**

1.前提，已安装好python，selenium，webdriver，可参考我的博客：https://blog.csdn.net/qq_39364032/article/details/109671761

2.下载该代码到本地，安装依赖（若已经有对应依赖，可忽略）

3.在企业微信中创建群机器人，获取到群机器人key值（可参考我的博客：https://blog.csdn.net/qq_39364032/article/details/112549075），
在config/envConfig文件中修改wwxKey值为自己的机器人key值

4.修改config/localhostConfig中的文件下载地址，为自己期望的地址

5.可运行实例，查看结果

6.示例运行成功后，可按照自己的需求，加入自己的网页地址，账号，密码等尝试，以下为一个例子

（1） 在config/envConfig 新增一个地址 `testUrl3 = 'https://www.biying.com/'`

（2）新建test03_biying.py测试文件，内部为截图相关代码，可参考现有的两个测试用例写

（3）在main.py 中加入 `suite3 = unittest.TestSuite()`

（4）在start函数下的`# 关闭浏览器`前加入
    `suite3.addTests(unittest.defaultTestLoader.discover('./', pattern='test03*.py'))`

在`if __name__ == '__main__':`的`# close window`前加入 `# run test2
    runTestSuite(suite3, "test3 必应")`

7.代码编写好后，可修改main.bat中的路径为自己的main.py的路径，在任务计划程序
中创建一个计划任务，每天定时执行main.bat

8.最后不要忘记，同时加入一个定时删除图片的计划任务，同样修改deleteImages.bat中的路径
为自己下载图片的地址，在计划任务中，创建一个计划任务，每天定时执行deleteImage.bat