"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/22 0:51'
"""
import pytest
from fourth.page.main_page import MainPage
from faker import Faker


class TestAddDepartment:
    """
    编写测试用例
    """
    faker = Faker(locale='zh_CN')
    def setup_class(self):
        self.main_page = MainPage()

    # 1. 实现测试数据和页面对象分离
    @pytest.mark.parametrize("department",[(faker.name())])
    def test_add_department(self, department):
        name = self.main_page.goto_add_address_book().goto_add_department().add_department(department)
        assert department in name