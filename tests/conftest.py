import pytest
from classes.operation import Operation


@pytest.fixture
def operation():
    operation = Operation(
        5,
        "2019-08-26T10:50:58.294041",
        "EXECUTED",
        {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }},
        "Перевод организации",
        "Счет 10848359769870775355",
        "Счет 10848359769870775355")
    return operation
