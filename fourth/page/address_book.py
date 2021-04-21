"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/19 23:47'
"""


from selenium.webdriver.common.by import By
from fourth.page.add_department import AddDepartment
from fourth.page.base import BasePage

class AddressBook(BasePage):
    def goto_add_department(self):
        """
        跳转到部门弹框
        :return:
        """
        self.find(By.CSS_SELECTOR, ".js_create_dropdown").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartment(self.driver)