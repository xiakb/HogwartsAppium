from appium.webdriver.common.mobileby import MobileBy
from page.pre_page import PrePage


class GoOutClockInPage(PrePage):
    """
    外出打卡页面
    """
    _go_out = (MobileBy.XPATH, "//*[contains(@text, '次外出')]")
    _Clock_in_success = (MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def go_out_clock_in(self):
        """
        外出打卡
        :return: 返回打开成功页面的源代码
        """
        # self.find_element(*self._go_out).click()
        self.base_page.displayed_and_click(*self._go_out)
        self.base_page.wait_for(*self._Clock_in_success)
        return self.base_page.driver.page_source

