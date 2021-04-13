from page.base_page import BasePage
from page.information_page import InformationPage
import allure
import pytest


@allure.feature("删除成员")
class TestDeleteMember:
    def setup_class(self):
        base_page = BasePage()
        self.app = InformationPage(base_page)

    def teardown_class(self):
        self.app.base_page.close_app()

    def teardown(self):
        self.app.back_information()

    @pytest.mark.parametrize(
        "name",
        ['木木1', '杉杉1'],
        ids=['delete_01', 'delete_02']
    )
    def test_delete_member(self, name):
        res = self.app.\
            goto_address_list_page().\
            goto_employee_information_page(name).\
            goto_personal_information_page().\
            goto_edit_member_page().delete_member().\
            get_member()
        assert name not in res
