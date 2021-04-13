"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/13 0:14'
"""
import yaml
import pytest
from Calculator import Calculator

@pytest.fixture(scope='class')
def connectCalc():
    print("setup")
    calc = Calculator()
    yield calc
    print("teardown")

@pytest.fixture(params=yaml.safe_load(open('../yaml/add.yaml'))['add_datas'],
                ids=yaml.safe_load(open('../yaml/add.yaml'))['ids'])
def get_add_datas(request):
    return request.param

@pytest.fixture(params=yaml.safe_load(open('../yaml/div.yaml'))['div_datas'],
                ids=yaml.safe_load(open('../yaml/div.yaml'))['ids'])
def get_div_datas(request):
    return request.param

# def pytest_collection_modifyitems(session, config, items: list):
#     items.reverse()
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')