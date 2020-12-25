from view.information_view import InformationView


class TestClockIn:
    def setup_class(self):
        self.information = InformationView()

    def teardown_class(self):
        self.information.close_app()

    def test_go_out_clock_in(self):
        pages = self.information.goto_workbench().goto_clock_in_view().goto_go_out_clock_in_view().go_out_clock_in()
        assert "外出打卡成功" in pages



