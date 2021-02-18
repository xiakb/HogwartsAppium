from appium.webdriver.common.mobileby import MobileBy
from page.pre_page import PrePage


class GoOutClockInPage(PrePage):
    """
    外出打卡页面
    """
    _go_out = (MobileBy.XPATH, "//*[contains(@text, '次外出')]")

    def go_out_clock_in(self):
        self.find_element(*self._go_out).click()
        self.display_wait("外出打卡成功")
        return self.driver.page_source

