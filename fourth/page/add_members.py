"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/19 23:48'
"""


from selenium.webdriver.common.by import By
from fourth.page.base import BasePage
from fourth.page.contact import ContactPage

class AddMemberPage(BasePage):
    # 设定为元祖
    # 页面元素不需要让 业务用例了解，所以要加私有
    __ele_username = (By.ID, "username")
    __ele_accid = (By.ID, "memberAdd_acctid")
    __ele_phone = (By.ID, "memberAdd_phone")

    def add_member(self, username, accid, phone):

        self.find(self.__ele_username).send_keys(username)
        self.find(*self.__ele_accid).send_keys(accid)
        self.find(*self.__ele_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    # def add_member_fail(self,username, accid, phone):
    #     self.driver.find_element(*self.__ele_username).send_keys(username)
    #     self.driver.find_element(*self.__ele_accid).send_keys(accid)
    #     self.driver.find_element(*self.__ele_phone).send_keys(phone)
    #     self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
    #     element = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
    #     error_list = []
    #     for ele in element:
    #         error_list.append(ele.text)
    #     return error_list
    #


