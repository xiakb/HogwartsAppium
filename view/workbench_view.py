from appium.webdriver.common.mobileby import MobileBy
from view.base_view import BaseView
from view.clock_in_view import ClockInView


class WorkbenchView(BaseView):
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

    def goto_clock_in_view(self):
        """
        跳转到打卡页面
        :return: 打卡页面
        """
        self.find_element(*self._clock_in).click()
        return ClockInView(self.driver)

