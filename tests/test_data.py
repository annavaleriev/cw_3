from classes.data import DataProcessor
from classes.operation import Operation
from settings import OPERATION_JSON_TEST


def test_get_executed_operations(data_processor):
    assert data_processor.get_executed_operations([{"state": "EXECUTED", "id": 1}, {"state": "CANCELED", "id": 2}]) == [
        {"state": "EXECUTED", "id": 1}]
    assert data_processor.get_executed_operations([]) == []
    assert data_processor.get_executed_operations([{"id": 1}, {"id": 2}]) == []


def test_sort_operations(data_processor):
    assert data_processor.sort_operations([]) == []
    assert data_processor.sort_operations(
        [
            {"date": "2023-09-14"},
            {"date": "2023-09-25"}
        ]
    ) == [{"date": "2023-09-25"}, {"date": "2023-09-14"}]
    assert data_processor.sort_operations([{}]) == [{}]


def test_get_five_operations(data_processor):
    assert data_processor.get_five_operations([]) == []
    assert data_processor.get_five_operations([
        {"date": "2023-09-16", "type": "EXECUTED"},
        {"date": "2023-09-15", "type": "EXECUTED"},
        {"date": "2023-09-14", "type": "EXECUTED"},
        {"date": "2023-09-13", "type": "EXECUTED"},
        {"date": "2023-09-12", "type": "EXECUTED"},
        {"date": "2023-09-11", "type": "EXECUTED"}
    ]) == [
               {"date": "2023-09-16", "type": "EXECUTED"},
               {"date": "2023-09-15", "type": "EXECUTED"},
               {"date": "2023-09-14", "type": "EXECUTED"},
               {"date": "2023-09-13", "type": "EXECUTED"},
               {"date": "2023-09-12", "type": "EXECUTED"}
           ]
    assert data_processor.get_five_operations(
        [
            {"date": "2023-09-16", "type": "EXECUTED"}
        ]
    ) == [{"date": "2023-09-16", "type": "EXECUTED"}]


def test_get_operation_objects(data_processor):
    assert data_processor.get_operation_objects([]) == []
    operation_dict = [
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        }
    ]
    operation_objects = data_processor.get_operation_objects(operation_dict)
    assert isinstance(operation_objects, list) is True
    assert isinstance(operation_objects[0], Operation) is True
    assert operation_objects[0].pk == 863064926
    assert len(operation_objects) == 1


def test_get_operations_list(data_processor):
    data_processor.path = OPERATION_JSON_TEST  # 'это пусть к тестовомку файлу
    operations_list = data_processor.get_operations_list()
    assert isinstance(operations_list, list)
    assert len(operations_list) == 5
    assert operations_list[0].operation_amount["amount"] == '97853.86'
    assert operations_list[1].date == '19.05.2019'
    assert operations_list[2].from_ == 'МИР 8021 88** **** 6544'
    assert operations_list[3].to == 'Счет ** 4188'
