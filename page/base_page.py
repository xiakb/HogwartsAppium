import os
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.common_fun import *
from common.desired_cap import desired_cap


class BasePage(object):
    def __init__(self):
        """
        初始化driver
        """
        self.driver = desired_cap()
        self.driver.implicitly_wait(8)

    def find(self, by, locator):
        """
        element定位器
        :param by: 定位方法
        :param locator: 元素属性值
        :return: element定位器
        """
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        """
        elements定位器
        :param by: 定位方法
        :param locator: 元素属性值
        :return: elements定位器
        """
        return self.driver.find_elements(by, locator)

    def scroll_find(self, text):
        """
        根据text属性值滚动查找元素
        :param text: 需要查找元素的text属性值
        :return: 查找到的元素
        """
        scroll = (MobileBy.ANDROID_UIAUTOMATOR, "new UiScrollable(new UiSelector()."
                                                "scrollable(true)."
                                                "instance(0))."
                                                "scrollIntoView(new UiSelector()."
                                                f"text({text}).instance(0));")
        return self.find(*scroll)

    def visible_and_clickable(self, *loc):
        """
        显示等待，判断某个元素是否可见并且是可以点击的
        :param loc: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(*loc))

    def whether_visible(self, *loc):
        """
        显示等待，判断元素是否可见
        :param loc: 需要等待的元素
        :return:
        """
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(*loc))

    def displayed_and_click(self, by, locator):
        """
        显示等待 \n
        判断元素是否可见，并点击该元素 \n
        :param by: 定位方法
        :param locator: 元素属性值
        :return:
        """
        for i in range(10):
            try:
                element = self.find(by, locator)
                if element.is_displayed():
                    element.click()
                    break
            except:
                pass
        else:
            pass

    def wait_for(self, by, locator):
        """
        显示等待（性别弹窗）
        :param by: 定位方法
        :param locator: 元素属性值
        :return:
        """
        def wait_ele_for(driver: WebDriver):
            eles = self.finds(by, locator)
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_ele_for)

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

    def swipe_up(self, start_x, start_y, end_x, end_y, duration, by, locator):
        """
        滑动查找元素
        :param start_x: 起始x坐标
        :param start_y: 起始y坐标
        :param end_x: 结束x坐标
        :param end_y: 结束y坐标
        :param duration: 等待时间
        :param by: 定位方法
        :param locator: 元素属性值
        :return:
        """
        i = 0
        while i < 10:
            try:
                self.find(by, locator).click()
                break
            except Exception as e:
                self.swipe(start_x, start_y, end_x, end_y, duration)
                i = i + 1

    def swipe_find(self, start_x, start_y, end_x, end_y, duration, by, locator):
        """
        滑动查找元素
        :param start_x: 起始x坐标
        :param start_y: 起始y坐标
        :param end_x: 结束x坐标
        :param end_y: 结束y坐标
        :param duration: 等待时间
        :param by: 定位方法
        :param locator: 元素属性值
        :return: 查找到的元素
        """
        self.driver.implicitly_wait(2)
        elements = self.finds(by, locator)
        while len(elements) == 0:
            self.swipe(start_x, start_y, end_x, end_y, duration)
            elements = self.finds(by, locator)
        return elements[0]

    def close_app(self):
        """
        关闭app
        :return:
        """
        return self.driver.close_app()

    def restart(self):
        """
        重启APP \n
        :return: self
        """
        self.driver.close_app()
        self.driver.launch_app()
        return self

    def quit(self):
        """
        停止APP或退出浏览器 \n
        :return:
        """
        self.driver.quit()

    def screenshot(self, module):
        """
        截图，并保存到指定的文件夹 \n
        :param module: 文件夹名称
        :return:
        """
        now_time = get_time()
        image_file = os.path.dirname(os.path.dirname(__file__)) + f'/screenshots/{module}_{now_time}.png'
        self.driver.get_screenshot_as_file(image_file)

    def latest_screenshot(self, screenshot_dir):
        """
        查找最新的截图，并返回 \n
        1、os.listdir() 用于返回指定文件夹包含的文件或文件夹的名称的列表 \n
        2、sort()按时间顺序对该文件夹下面的文件进行排序 \n
        3、os.path.join()输出最新的报告路径 \n
        :param screenshot_dir: 接收存放截图的路径
        :return: 返回最新的截图
        """
        lists = os.listdir(screenshot_dir)
        lists.sort(key=lambda fn: os.path.getatime(screenshot_dir + '//' + fn))
        picture = os.path.join(screenshot_dir, lists[-1])
        return picture

