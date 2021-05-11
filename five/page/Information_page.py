"""
__author__ = 'ceshiren_szr'
__time__ = '2021/4/27 23:56'
"""
from appium.webdriver.common.mobileby import MobileBy
from five.page.base import BasePage

class InformationPage(BasePage):
    __details = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout")

    def goto_Information_details(self):
        self.log.info("点击更多按键，跳转到成员信息详情页面")
        self.find(self.__details).click()
        return self.Information_details()

    def Information_details(self):
        self.log.info("点击编辑成员按键，跳转到编辑成员页面")
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        from five.page.edit_member_page import EditMemberPage
        return EditMemberPage(self.driver)

