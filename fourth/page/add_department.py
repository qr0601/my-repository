"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/19 23:49'
"""

from selenium.webdriver.common.by import By
from fourth.page.base import BasePage


class AddDepartment(BasePage):


    def add_department(self, department):

        self.find((By.CSS_SELECTOR, '.form>div:nth-child(1)>input')).send_keys(department)
        self.find((By.CSS_SELECTOR, '.js_parent_party_name')).click()
        self.find(By.CSS_SELECTOR,".qui_dialog_body.ww_dialog_body [id='1688850937136770_anchor']").click()
        self.find(By.CSS_SELECTOR, '.member_tag_dialog>.qui_dialog_foot>a:nth-child(1)').click()
        self.refresh()
        department_name =  self.finds(By.CSS_SELECTOR,'.jstree-children')
        name_list= []
        # 遍历元素列表，通过元素的text 属性，提取文本数据信息
        for name in department_name:
            name_list.append(name.text)
        name_result = name_list[0].split('\n ')
        return name_result
