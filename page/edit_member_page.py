from appium.webdriver.common.mobileby import MobileBy
from page.pre_page import PrePage


class EditMemberPage(PrePage):
    """编辑成员页"""
    _delete_member = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/esd' and @text='删除成员']")
    _confirm = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/bpc' and @text='确定']")

    def click_delete_member(self):
        """点击删除成员"""
        self.base_page.find(*self._delete_member).click()

    def click_confirm(self):
        """点击确认"""
        self.base_page.find(*self._confirm).click()

    def delete_member(self):
        """
        删除成员，并回到通讯录页面
        :return: 通讯录页面
        """
        from page.address_list_page import AddressListPage
        self.click_delete_member()
        self.click_confirm()
        return AddressListPage(self.base_page)
