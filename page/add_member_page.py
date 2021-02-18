from appium.webdriver.common.mobileby import MobileBy
from page.pre_page import PrePage


class AddMemberPage(PrePage):
    """
    添加成员页面
    """
    _manually_add = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _address_list = (MobileBy.XPATH, "//*[@esource-id='com.tencent.wework:id/i63']")

    def goto_manually_add_page(self):
        """
        跳转到手动添加页面
        :return: 手动添加页面
        """
        self.find_element(*self._manually_add).click()
        return ManuallyAddPage(self.base_page)

    def goto_address_list_page(self):
        """
        返回到通讯录页面
        :return: 通讯录页面
        """
        from page.address_list_page import AddressListPage
        self.find_element(*self._address_list).click()
        return AddressListPage(self.base_page)


class ManuallyAddPage(PrePage):
    """
    手动添加成员页面
    """
    _username = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/..//*[@text='必填']")
    _gender = (MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
    _female = (MobileBy.XPATH, "//*[@text='女'")
    _male = (MobileBy.XPATH, "//*[@text='男'")
    _phone_number = (MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']")
    _save = (MobileBy.XPATH, "//*[@text='保存' and @resource-id='com.tencent.wework:id/i6k']")

    def type_username(self, username):
        """
        输入姓名
        :param username: 要输入的姓名
        :return:
        """
        self.find_element(*self._username).clear()
        self.find_element(*self._username).send_keys(username)

    def select_male(self):
        """
        性别选择男
        :return:
        """
        self.wait_for(*self._female)
        self.find_element(*self._male).click()

    def select_female(self):
        """
        性别选择女
        :return:
        """
        self.wait_for(*self._female)
        self.find_element(*self._female).click()

    def type_phone_number(self, phone):
        """
        输入手机号
        :param phone: 要输入的手机号
        :return:
        """
        self.find_element(*self._phone_number).clear()
        self.find_element(*self._phone_number).send_keys(phone)

    def click_save(self):
        """
        点击保存
        :return:
        """
        self.find_element(*self._save).click()

    def add_male_member(self, username, phone):
        """
        添加男成员
        :param username: 要输入的姓名
        :param phone: 要输入的手机号
        :return: 通讯录页面
        """
        self.type_username(username)
        self.select_male()
        self.type_phone_number(phone)
        self.click_save()
        return AddMemberPage(self.base_page)

    def add_female_member(self, username, phone):
        """
        添加女成员
        :param username: 要输入的姓名
        :param phone: 要输入的手机号
        :return: 通讯录页面
        """
        self.type_username(username)
        self.select_female()
        self.type_phone_number(phone)
        self.click_save()
        return AddMemberPage(self.base_page)

