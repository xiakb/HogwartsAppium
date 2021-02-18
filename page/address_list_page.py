from appium.webdriver.common.mobileby import MobileBy
from page.add_member_page import AddMemberPage
from page.pre_page import PrePage


class AddressListPage(PrePage):
    """
    通讯录页面
    """
    _add_mem = (MobileBy.XPATH, "//*[@text='添加成员']")
    _member_information = (MobileBy.XPATH,
                           "//*[@resource-id='com.tencent.wework:id/egr']//*[@class='android.widget.TextView']")

    def goto_add_member_page(self):
        """
        跳转到添加成员页面
        :return: 添加成员页面
        """
        # self.find_element(*self._add_mem).click()
        self.scroll_find("添加成员").click()
        return AddMemberPage(self.base_page)

    def get_member(self):
        """
        获取成员列表
        :return: 成员列表
        """
        member_list = self.find_elements(*self._member_information)
        member_list_res = [i.text for i in member_list]
        return member_list_res

