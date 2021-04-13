from appium.webdriver.common.mobileby import MobileBy
from page.personal_information_page import PersonalInformationPage
from page.pre_page import PrePage


class EmployeeInformationPage(PrePage):
    """员工个人信息页"""
    _edit = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/iga']")

    def goto_personal_information_page(self):
        """
        跳转到个人信息编辑页
        :return: 人信息编辑页
        """
        self.base_page.find(*self._edit).click()
        return PersonalInformationPage(self.base_page)
