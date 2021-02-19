from page.base_page import BasePage
from page.information_page import InformationPage


class TestAddMember:
    def setup_class(self):
        base_page = BasePage()
        self.information = InformationPage(base_page)

    def teardown_class(self):
        self.information.close_app()

    def teardown(self):
        self.information.back_information()

    def test_manual_add_male_member(self):
        """
        测试添加男成员
        :return:
        """
        res = self.information.\
            goto_address_list_page().\
            goto_add_member_page().\
            goto_manually_add_page().\
            add_male_member('木木1', '15800000001').\
            goto_address_list_page().\
            get_member()
        assert '木木1' in res

    def test_manual_add_female_member(self):
        """
        测试添加女成员
        :return:
        """
        res = self.information.\
            goto_address_list_page().\
            goto_add_member_page().\
            goto_manually_add_page().\
            add_female_member('杉杉1', '15900000001').\
            goto_address_list_page().\
            get_member()
        assert '杉杉1' in res
