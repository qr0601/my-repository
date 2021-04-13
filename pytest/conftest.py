"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/13 0:14'
"""
import pytest
from Calculator import Calculator

@pytest.fixture()
def connectCalc():
    print("setup")
    calc = Calculator()
    yield calc
    print("teardown")