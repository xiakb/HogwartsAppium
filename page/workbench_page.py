from appium.webdriver.common.mobileby import MobileBy
from page.clock_in_page import ClockInPage
from page.pre_page import PrePage


class WorkbenchPage(PrePage):
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

    _punch_card = (MobileBy.XPATH, "//*[@text='打卡' and @resource-id='com.tencent.wework:id/fcc']")

    def goto_clock_in_page(self):
        """
        跳转到打卡页面
        :return: 打卡页面
        """
        # self.find_element(*self._clock_in).click()
        # self.scroll_find("打卡").click()
        s = self.get_window_size()
        x = s['width'] * 0.5
        y1 = s['height'] * 0.75
        y2 = s['height'] * 0.25
        self.swipe_up(x, y1, x, y2, 1000, *self._punch_card)
        return ClockInPage(self.base_page)

