from appium.webdriver.common.mobileby import MobileBy
from page.add_member_page import AddMemberPage
from page.employee_information_page import EmployeeInformationPage
from page.pre_page import PrePage
import time


class AddressListPage(PrePage):
    """
    通讯录页面
    """
    _add_mem = (MobileBy.XPATH, "//*[@text='添加成员']")
    _member_information = (MobileBy.XPATH,
                           "//*[@resource-id='com.tencent.wework:id/bdf']//*[@class='android.widget.TextView']")

    def goto_add_member_page(self):
        """
        跳转到添加成员页面
        :return: 添加成员页面
        """
        s = self.base_page.get_window_size()
        x = s['width'] * 0.5
        y1 = s['height'] * 0.75
        y2 = s['height'] * 0.25
        self.base_page.swipe_up(x, y1, x, y2, 1000, *self._add_mem)
        return AddMemberPage(self.base_page)

    def get_member(self):
        """
        获取成员列表
        :return: 成员列表
        """
        time.sleep(2)
        member_list = self.base_page.finds(*self._member_information)
        member_list_res = [i.text for i in member_list]
        return member_list_res

    def goto_employee_information_page(self, username):
        """
        跳转到员工个人信息页
        :return: 员工个人信息页
        """
        if username in self.get_member():
            self.base_page.find(MobileBy.XPATH, f"//*[@text='{username}']").click()
            return EmployeeInformationPage(self.base_page)

