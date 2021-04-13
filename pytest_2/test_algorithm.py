"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/10 8:00'
"""
import pytest


class TestCal:
    @pytest.mark.run(order = 2)
    def test_add(self,connectCalc,get_add_datas):
        assert get_add_datas[2] == round(connectCalc.add(get_add_datas[0], get_add_datas[1]),1)

    @pytest.mark.run(order = 1)
    def test_div(self, connectCalc,get_div_datas):
        try:
            assert get_div_datas[2] == round(connectCalc.div(get_div_datas[0], get_div_datas[1]),1)
        except ZeroDivisionError:
                print(get_div_datas[2])




