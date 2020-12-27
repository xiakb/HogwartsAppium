from appium.webdriver.common.mobileby import MobileBy
from page.base_page import BasePage
from page.clock_in_page import ClockInPage


class WorkbenchPage(BasePage):
    """
    工作台页
    """
    _clock_in = (MobileBy.ANDROID_UIAUTOMATOR, "new UiScrollable("
                                               "new UiSelector()."
                                               "scrollable(true)."
                                               "instance(0))."
                                               "scrollIntoView("
                                               "new UiSelector()."
                                               "text('打卡')."
                                               "instance(0));")

    def goto_clock_in_page(self):
        """
        跳转到打卡页面
        :return: 打卡页面
        """
        # self.find_element(*self._clock_in).click()
        self.scroll_find("打卡").click()
        return ClockInPage(self.driver)

