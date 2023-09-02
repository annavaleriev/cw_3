import pytest
from classes.operation import Operation


# test_operation_list = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#     ]

pk = 441945886
state = "EXECUTED"
date = "2019-08-26T10:50:58.294041"
operationAmount =  {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }
description =  "Перевод организации"
from_ = "Maestro 1596837868705199"
to = "Счет 64686473678894779589"

# pk, state, date, operationAmount, description, from_, to
@pytest.fixture
def test_fixture():
    return pk, state, date, operationAmount, description, from_, to


def test_convert_date(test_fixture):
    test_operation_a = Operation(pk, state, date, operationAmount, description, from_, to)
    assert test_operation_a.convert_date("2019-08-26T10:50:58.294041") == "26.08.2019"
