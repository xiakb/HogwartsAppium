from page.base_page import BasePage
from page.information_page import InformationPage


class TestClockIn:
    def setup_class(self):
        base_page = BasePage()
        self.app = InformationPage(base_page)

    def teardown_class(self):
        self.app.base_page.close_app()

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

