from page.base_page import BasePage
from page.information_page import InformationPage
import allure


@allure.feature("考勤打卡")
class TestClockIn:
    def setup_class(self):
        base_page = BasePage()
        self.app = InformationPage(base_page)

    def teardown_class(self):
        self.app.base_page.close_app()

    @allure.story("外出打卡")
    def test_go_out_clock_in(self):
        """
        外出打卡测试
        :return:
        """
        pages = self.app.\
            goto_workbench_page().\
            goto_clock_in_page().\
            goto_go_out_clock_in_page().\
            go_out_clock_in()
        assert "外出打卡成功" in pages

