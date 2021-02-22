from appium.webdriver.common.mobileby import MobileBy
from page.go_out_clock_in_page import GoOutClockInPage
from page.pre_page import PrePage


class ClockInPage(PrePage):
    """
    打卡页面
    """
    _go_out_clock_in = (MobileBy.XPATH, "//*[@text='外出打卡']")

    def goto_go_out_clock_in_page(self):
        """
        跳转到外出打卡页面
        :return: 外出打卡页面
        """
        self.base_page.find(*self._go_out_clock_in).click()
        return GoOutClockInPage(self.base_page)

