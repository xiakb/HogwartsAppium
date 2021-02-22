from appium import webdriver
from common.common_fun import *


def desired_cap():
    """
    启动对应APP
    :return: driver
    """
    data = get_data("desired_caps.yaml")
    # 启动app参数
    desired_caps = {
        'platformName': data['platformName'],
        'platformVersion': data['platformVersion'],
        'deviceName': data['deviceName'],
        'noReset': data['noReset'],
        # 'unicodeKeyboard': data['unicodeKeyboard'],
        # 'resetKeyboard': data['resetKeyboard'],
        'dontStopAppOnReset': data['dontStopAppOnReset'],
        'settings[waitForIdleTimeout]': data['settings[waitForIdleTimeout]'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'ensureWebviewsHavePages': data['ensureWebviewsHavePages']
        # 'newCommandTimeout': data['newCommandTimeout']
    }

    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    return driver


if __name__ == '__main__':
    desired_cap()