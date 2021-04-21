"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/19 23:45'
"""

from selenium.webdriver.common.by import By
from fourth.page.add_members import AddMemberPage
from fourth.page.address_book import AddressBook
from fourth.page.base import BasePage


class MainPage(BasePage):
    """
    用公共方法代表UI所提供的功能
    """

    def goto_contact(self):
        """
        跳转到通讯录页面
        :return:
        """
        pass

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        # 返回要跳转页面的实例对象

        self.find(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()
        return AddMemberPage(self.driver)

    def goto_add_address_book(self):
        """
        跳转到通讯录页面
        :return:
        """
        self.find(By.XPATH,'//*[@id="menu_contacts"]').click()
        return AddressBook(self.driver)