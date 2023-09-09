import json
from settings import OPERATION_JSON_TEST

import pytest

from classes.data import DataProcessor
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


@pytest.fixture
def test_json():
    with open(OPERATION_JSON_TEST) as file:
        test_json_load = json.load(file)
        return test_json_load


@pytest.fixture
def executed_operations():
    with open('test_executed_operations.json') as file:
        test_executed_operations = json.load(file)
        return test_executed_operations

#     return [
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   },
#   {
#     "id": 142264268,
#     "state": "EXECUTED",
#     "date": "2019-04-04T23:20:05.206878",
#     "operationAmount": {
#       "amount": "79114.93",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод со счета на счет",
#     "from": "Счет 19708645243227258542",
#     "to": "Счет 75651667383060284188"
#   },
#   {
#     "id": 556488059,
#     "state": "EXECUTED",
#     "date": "2019-05-17T01:50:00.166954",
#     "operationAmount": {
#       "amount": "74604.56",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод с карты на карту",
#     "from": "МИР 8021883699486544",
#     "to": "Visa Gold 8702717057933248"
#   },
#   {
#     "id": 179194306,
#     "state": "EXECUTED",
#     "date": "2019-05-19T12:51:49.023880",
#     "operationAmount": {
#       "amount": "6381.58",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "МИР 5211277418228469",
#     "to": "Счет 58518872592028002662"
#   },
#   {
#     "id": 667307132,
#     "state": "EXECUTED",
#     "date": "2019-07-13T18:51:29.313309",
#     "operationAmount": {
#       "amount": "97853.86",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод с карты на счет",
#     "from": "Maestro 1308795367077170",
#     "to": "Счет 96527012349577388612"
#   }
# ]


# @pytest.fixture
# def data_processor():
#     test_get_executed_operations = DataProcessor(test_json())
#     return test_get_executed_operations

@pytest.fixture
def sorted_operations():
    return [
{
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
        "amount": "97853.86",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
},
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 556488059,
            "state": "EXECUTED",
            "date": "2019-05-17T01:50:00.166954",
            "operationAmount": {
                "amount": "74604.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "to": "Visa Gold 8702717057933248"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }
    ]

@pytest.fixture
def last_five__operations():
    return [
{
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
        "amount": "97853.86",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
},
        {
            "id": 179194306,
            "state": "EXECUTED",
            "date": "2019-05-19T12:51:49.023880",
            "operationAmount": {
                "amount": "6381.58",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "МИР 5211277418228469",
            "to": "Счет 58518872592028002662"
        },
        {
            "id": 556488059,
            "state": "EXECUTED",
            "date": "2019-05-17T01:50:00.166954",
            "operationAmount": {
                "amount": "74604.56",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8021883699486544",
            "to": "Visa Gold 8702717057933248"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]