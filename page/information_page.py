from appium.webdriver.common.mobileby import MobileBy
from page.address_list_page import AddressListPage
from page.pre_page import PrePage
from page.workbench_page import WorkbenchPage


class InformationPage(PrePage):
    """
    消息页面
    """
    _workbench = (MobileBy.XPATH, "//*[@text='工作台' and @resource-id='com.tencent.wework:id/en5']")
    # _workbench = (MobileBy.XPATH, "//*[@text='工作台']")
    _address = (MobileBy.XPATH, "//*[@text='通讯录' and @resource-id='com.tencent.wework:id/en5']")
    _information = (MobileBy.XPATH, "//*[@text='消息' and @resource-id='com.tencent.wework:id/en5']")

    def goto_workbench_page(self):
        """
        跳转到工作台页面
        :return: 工作台页面
        """
        self.find_element(*self._workbench).click()
        return WorkbenchPage(self.base_page)

    def goto_address_list_page(self):
        """
        跳转到通讯录页面
        :return: 通讯录页面
        """
        self.find_element(*self._address).click()
        return AddressListPage(self.base_page)

    def back_information(self):
        """
        返回消息页面
        :return:
        """
        self.find_element(*self._information).click()

