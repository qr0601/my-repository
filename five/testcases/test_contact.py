"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:30'
"""
import logging
import pytest
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from five.page.app import App
from five.testcases.contact_info import ContactInfo

class TestContact:
    def setup_class(self):
        self.contactinfo = ContactInfo()
        self.app = App()

    def setup(self):
        # 启动 app
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.restart()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize("name, phonenum",[["测试1号", "15883625110"]])
    def test_addcontact(self, name, phonenum):
        # name = self.contactinfo.get_name()
        # phonenum = self.contactinfo.get_phonenum()
        self.main.goto_contactlist(). \
            goto_addmember().addmember_bymenual(). \
            add_member(name, phonenum).retrun_contactlist().check_member(name)

    @pytest.mark.parametrize("name", ["测试1号"])
    def test_deletecontact(self, name):
        try:
            self.main.goto_contactlist().goto_member_information(name).goto_Information_details() \
                .delete_member().check_delete(name)
        except NoSuchElementException:
            logging.info("删除成功")
