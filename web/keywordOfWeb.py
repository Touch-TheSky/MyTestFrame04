# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

class KeywordOfWeb():
    def __init__(self):
        self.driver = None
        self.txt = ''

    def openBrower(self,br='gc',dr='../lib/chromedriver'):
        '''
        打开浏览器
        :param br: 浏览器类型 默认谷歌浏览器
        :param dr: 浏览器driver路径
        :return:
        '''
        if br == "gc":
            opt = Options()
            opt.add_argument('--user-data-dir=%s\\AppData\\Local\\Google'
                             '\\Chrome\\User Data' % os.environ["USERPROFILE"])
            self.driver = webdriver.Chrome(options=opt,executable_path=dr)
            self.driver.implicitly_wait(10)

        else:
            print("功能暂未实现，敬请期待！")

    def geturl(self,url):
        """
        打开网页
        :param url: 网址
        :return:
        """
        self.driver.get(url)

    def input(self,xpath,content):
        """
        输入
        :param xpath:输入框的元素路径
        :param content: 输入的内容
        :return:
        """
        self.__findeleXpath(xpath).send_keys(content)

    def click(self,xpath):
        """
        点击方法
        :param xpath:点击元素的xpath路径
        :return:
        """
        self.__findeleXpath(xpath).click()

    def gettext(self,xpath):
        """
        获取元素文本内容
        :param xpath: 元素的xpath路径
        :return:
        """
        self.txt = self.__findeleXpath(xpath).text
        return self.txt

    def asserteqiue(self,expect_value,msg):
        """
        元素校验
        :param expect_value:
        :param msg:
        :return:
        """
        if self.txt == expect_value:
            print(msg + "校验成功")
        else:
            print(msg + "校验失败")

    def __findeleXpath(self,xpath):
        """查找元素"""
        ele = self.driver.find_element_by_xpath(xpath)
        return ele

    def halt(self,t=1):
        """固定等待时长"""
        if t is None or t == '':
            t = 1
        else:
            t = int(t)
        time.sleep(t)

    def quit(self):
        """关闭浏览器"""
        self.driver.quit()










