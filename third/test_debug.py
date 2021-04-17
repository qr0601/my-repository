"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/17 22:31'
"""
import yaml
from selenium import webdriver

class TestDebug():
    def test_weixin(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

        # 获取cookie信息
        cookie = self.driver.get_cookies()
        # 把cookie存如yaml文件内
        with open("data.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f)