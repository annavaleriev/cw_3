from classes.operation import Operation


def test_convert_date():
    test_operation = Operation(5, "2019-08-26T10:50:58.294041", "fhhfhf", {}, "fhhfhf", "jfjfjjf", "jfjfjfj")
    assert test_operation.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_hide_card_number_first():
    test_card = Operation(5, "2019-08-26T10:50:58.294041", "fhhfhf", {}, "fhhfhf", "jfjfjjf", "jfjfjjf")
    assert test_card.hide_card_number("Счет 35383033474447895560") == "Счет ** 5560"


def test_hide_card_number_second():
    test_card = Operation(5, "2019-08-26T10:50:58.294041", "fhhfhf", {}, "fhhfhf", "jfjfjjf", "jfjfjjf")
    assert test_card.hide_card_number("Visa Classic 2842872476739012") == "Visa Classic 2842 87** **** 9012"
