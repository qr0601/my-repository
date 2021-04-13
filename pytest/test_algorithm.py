"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/10 8:00'
"""
import pytest
import yaml


class TestCal:
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('../yaml/add.yaml'))['add_datas'],
                             ids=yaml.safe_load(open('../yaml/add.yaml'))['ids'])
    def test_add(self, a, b, expect,connectCalc):
        assert expect == round(connectCalc.add(a, b),1)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('../yaml/div.yaml'))['div_datas'],
                             ids=yaml.safe_load(open('../yaml/div.yaml'))['ids'])
    def test_div(self, a, b, expect,connectCalc):
        try:
            assert expect == round(connectCalc.div(a, b),1)
        except ZeroDivisionError:
                print(expect)




