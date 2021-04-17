"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/17 22:23'
"""
import pytest
from faker import Faker
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="class", autouse=True)
def faker():
    faker = Faker(locale='zh_CN')
    return faker
