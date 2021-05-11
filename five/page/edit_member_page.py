"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:54'
"""
from appium.webdriver.common.mobileby import MobileBy
from five.page.base import BasePage

class EditMemberPage(BasePage):

    def add_member(self, name, phonenum):
        # self.find(MobileBy.XPATH,
        #           "//*[contains(@text,'姓名')]/..//*[@text='必填']").click()
        self.log.info(f"输入姓名：{name}")
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'姓名')]/..//android.widget.EditText").send_keys(name)
        self.log.info(f"输入手机号：{phonenum}")
        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phonenum)
        self.log.info("点击保存")
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from five.page.add_member_page import AddMemberPage
        self.log.info("跳转到添加成员页面")
        return AddMemberPage(self.driver)

    def delete_member(self):
        self.log.info("点击删除成员按键，弹出删除提示框")
        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        # self.swipe_find('删除成员').click()
        self.log.info("点击确定，跳转到列表页面")
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        from five.page.contactlist_page import ContactListPage
        return ContactListPage(self.driver)
