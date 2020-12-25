from appium.webdriver.common.mobileby import MobileBy
from view.base_view import BaseView
from view.go_out_clock_in_view import GoOutClockIn


class ClockInView(BaseView):
    """
    打卡页面
    """
    _go_out_clock_in = (MobileBy.XPATH, "//*[@text='外出打卡']")

    def goto_go_out_clock_in_view(self):
        """
        跳转到外出打卡页面
        :return: 外出打卡页面
        """
        self.find_element(*self._go_out_clock_in).click()
        return GoOutClockIn(self.driver)

