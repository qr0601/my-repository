"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:25'
"""

# 主页面
from appium.webdriver.common.mobileby import MobileBy
from five.page.base import BasePage
from five.page.contactlist_page import ContactListPage

class MainPage(BasePage):
    contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        # click 通讯录
        self.find(*self.contact_element).click()
        return ContactListPage(self.driver)
