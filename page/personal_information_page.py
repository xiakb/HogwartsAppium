from appium.webdriver.common.mobileby import MobileBy
from page.edit_member_page import EditMemberPage
from page.pre_page import PrePage


class PersonalInformationPage(PrePage):
    """个人信息页面"""
    _edit_member = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bct' and @text='编辑成员']")

    def goto_edit_member_page(self):
        """
        跳转到编辑成员页
        :return: 编辑成员页
        """
        self.base_page.find(*self._edit_member).click()
        return EditMemberPage(self.base_page)
