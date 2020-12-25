from appium.webdriver.common.mobileby import MobileBy
from view.base_view import BaseView


class GoOutClockIn(BaseView):
    """
    外出打卡页面
    """
    _go_out = (MobileBy.XPATH, "//*[contains(@text, '次外出')]")

    def go_out_clock_in(self):
        self.find_element(*self._go_out).click()
        self.wait_click("外出打卡成功")
        return self.driver.page_source

