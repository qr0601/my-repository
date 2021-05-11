"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:30'
"""
from time import sleep
from five.page.Information_page import InformationPage
from five.page.add_member_page import AddMemberPage
from five.page.base import BasePage


class ContactListPage(BasePage):

    def goto_addmember(self):
        self.log.info("点击添加成员，跳转到添加成员页面")
        self.swipe_find('添加成员').click()
        return AddMemberPage(self.driver)

    def goto_member_information(self, name):
        self.log.info(f"在通讯录列表点击成员：{name},跳转到成员信息页面")
        self.swipe_find(name).click()
        return InformationPage(self.driver)

    def check_delete(self, name):
        sleep(2)
        self.log.info(f"删除{name}成员成功")
        return self.swipe_find(name)

    def check_member(self, name):
        self.swipe_upward_find(name)
        return True
