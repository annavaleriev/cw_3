from operation import Operation


def test_convert_date():
    test_operation = Operation(5, "2019-08-26T10:50:58.294041", "fhhfhf", {}, "fhhfhf", "jfjfjjf", "jfjfjfj")
    assert test_operation.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"

