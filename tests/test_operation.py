class TestOperation:

    def test_convert_date(self, operation):
        assert operation.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"

    def test_hide_card_number_first(self, operation):
        assert operation.hide_card_number("Счет 35383033474447895560") == "Счет ** 5560"

    def test_hide_card_number_second(self, operation):
        assert operation.hide_card_number("Visa Classic 2842872476739012") == "Visa Classic 2842 87** **** 9012"

    def test_final_text(self, operation):
        assert operation.__str__() == "26.08.2019 Перевод организации\nСчет ** 5355 -> Счет ** 5355\n 43318.34 руб.\n"
