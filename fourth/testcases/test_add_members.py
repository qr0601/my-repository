"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/21 22:59'
"""

import pytest
from fourth.page.main_page import MainPage
from faker import Faker


class TestAddMember:
    """
    编写测试用例
    """
    faker = Faker(locale='zh_CN')
    def setup_class(self):
        self.main_page = MainPage()

    # 1. 实现测试数据和页面对象分离
    @pytest.mark.parametrize("username, accid, phone",[(faker.name(), faker.pystr(), faker.phone_number())])
    def test_add_member(self, username, accid, phone):
        name_list = self.main_page.goto_add_member().add_member(username, accid, phone).get_contact_list()
        assert username in name_list

    # @pytest.mark.parametrize("username, accid, phone",[("伊泽瑞尔1", "00901", "13344445555")])
    # def test_add_member_fail(self, username, accid, phone):
    #     data_list = self.main_page.goto_add_member().add_member_fail(username, accid, phone)
    #     err = [i for i in data_list if i != ""]
    #     assert "伊泽瑞尔" in err[0]

