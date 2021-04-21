"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/19 23:38'
"""

import yaml
from selenium import webdriver


class BasePage:
    """
    把页面重复的步骤抽离出来，封装，比如driver 的实例化
    """
    def __init__(self, base_driver=None):
        """
        driver 重复实例化会 导致页面启动多次
        解决driver 重复实例化的问题
        :param base_driver:
        """
        if base_driver == None:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            # 访问扫码登录页面
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.driver.maximize_window()
            with open("../yaml/cookie.yaml", encoding="UTF-8") as f:
                yaml_data = yaml.safe_load(f)
                for cookie in yaml_data:
                    self.driver.add_cookie(cookie)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def find(self, by, locate = None):
        """
        :param by: 定位方式 css, xpath, id
        :param locate: 元素定位信息
        :return:
        """
        if locate == None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, locate)

    def finds(self, by, locate = None):
        if locate == None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locate)

    def refresh(self):
        self.driver.refresh()




