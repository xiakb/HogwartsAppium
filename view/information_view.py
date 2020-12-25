from appium.webdriver.common.mobileby import MobileBy
from view.base_view import BaseView
from view.workbench_view import WorkbenchView


class InformationView(BaseView):
    """
    消息页面
    """
    _workbench = (MobileBy.XPATH, "//*[@text='工作台']")

    def goto_workbench(self):
        """
        跳转到工作台页面
        :return: 工作台页面
        """
        self.find_element(*self._workbench).click()
        return WorkbenchView(self.driver)

