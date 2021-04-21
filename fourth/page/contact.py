"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/21 22:55'
"""

from selenium.webdriver.common.by import By
from fourth.page.base import BasePage

class ContactPage(BasePage):
    def get_contact_list(self):
        # 获取的是元素列表
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list= []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for ele in ele_list:
            name_list.append(ele.text)
        return name_list

