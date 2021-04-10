"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/10 8:00'
"""
import pytest
import yaml
from Calculator import Calculator

class TestCal:

    def setup_class(self):
        print("setup")
        self.calc = Calculator()

    def teardown_class(self):
        print("teardown")

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./add.yaml')), ids=['int', 'float', 'zeronum'])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('./div.yaml')), ids=['int', 'zeronum', 'float'])
    def test_div(self, a, b, expect):
        if b != 0:
            assert expect == self.calc.div(a, b)
        else:
            try:
                self.calc.div(a, b)
            except Exception as err:
                assert expect in str(err)




