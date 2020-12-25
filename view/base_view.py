from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.common_fun import *


class BaseView(object):
    def __init__(self, driver=None):
        """
        初始化driver
        :param driver:
        """
        if driver is None:
            self.driver = desired_cap()
        else:
            self.driver = driver
        self.driver.implicitly_wait(8)

    def find_element(self, *loc):
        """
        element定位器
        :param loc: 可变参数，元素属性值
        :return: element定位器
        """
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        """
        elements定位器
        :param loc: 可变参数，元素属性值
        :return: elements定位器
        """
        return self.driver.find_elements(*loc)

    def wait_click(self, locator):
        """
        显示等待
        :param locator: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def get_window_size(self):
        """
        获取屏幕尺寸
        :return:
        """
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        """
        屏幕滑动
        :param start_x: 起始点的横坐标
        :param start_y: 起始点的纵坐标
        :param end_x: 结束点的横坐标
        :param end_y: 结束点的纵坐标
        :param duration: 持续时长
        :return:
        """
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def close_app(self):
        """
        关闭app
        :return:
        """
        return self.driver.close_app()

