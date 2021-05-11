"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:45'
"""

from appium.webdriver.common.mobileby import MobileBy
from five.page.base import BasePage
from five.page.edit_member_page import EditMemberPage

class AddMemberPage(BasePage):

    def addmember_bymenual(self):
        # click 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditMemberPage(self.driver)

    def find_toast(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成功']")
        # return True

    def retrun_contactlist(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/h86").click()
        from five.page.contactlist_page import ContactListPage
        return ContactListPage(self.driver)
