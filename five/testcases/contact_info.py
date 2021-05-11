"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:32'
"""

from faker import Faker


class ContactInfo:
    def __init__(self):
        self.faker = Faker('zh_CN')

    def get_name(self):
        name = self.faker.name()
        return name

    def get_phonenum(self):
        phonenum = self.faker.phone_number()
        return phonenum