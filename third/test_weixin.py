"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/15 1:11'
"""

import yaml
from selenium.webdriver.common.by import By


class Testweixin:
    def test_add(self,driver,faker):
        # 访问扫码登录页面
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        driver.maximize_window()
        with open("data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # 点击首页页面中下方常用入口中的添加成员按钮
        driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        # 添加成员基本信息
        driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(faker.name())
        driver.find_element(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys(faker.pystr())
        driver.find_element(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys(faker.phone_number())
        driver.find_element(By.LINK_TEXT,'保存').click()
        assert driver.find_element(By.LINK_TEXT,'修改名称')




