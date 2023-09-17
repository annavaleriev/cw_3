from classes.data import DataProcessor


def test_get_executed_operations():
    data_processor = DataProcessor('')
    assert data_processor.get_executed_operations([{"state": "EXECUTED", "id": 1}, {"state": "CANCELED", "id": 2}]) == [
        {"state": "EXECUTED", "id": 1}]
    assert data_processor.get_executed_operations([]) == []
    assert data_processor.get_executed_operations([{"id": 1}, {"id": 2}]) == []


def test_sort_operations():
    data_processor = DataProcessor('')
    assert data_processor.sort_operations([]) == [] # мне нужна эта строчка? и без неё работает?
    assert data_processor.sort_operations([{"date": "2023-09-15", "type": "EXECUTED"}, {"date": "2023-09-14", "type": "EXECUTED"}]) == [{"date": "2023-09-15", "type": "EXECUTED"}, {"date": "2023-09-14", "type": "EXECUTED"}]

    # executed_operations = [
    #     {"date": "2023-09-15", "type": "EXECUTED"},
    #     {"date": "2023-09-14", "type": "EXECUTED"},
    #     {"date": "2023-09-16", "type": "EXECUTED"},
    # ]
    # sorted_operations = sort_operations(executed_operations)
    # expected_result = [
    #     {"date": "2023-09-16", "type": "EXECUTED"},
    #     {"date": "2023-09-15", "type": "EXECUTED"},
    #     {"date": "2023-09-14", "type": "EXECUTED"},
    # ]
    # assert sorted_operations == expected_result
    #
    # # executed_operations = [{"date": "2023-09-15", "type": "EXECUTED"}]
    # # sorted_operations = data_processor.sort_operations(executed_operations)
    # # # assert sorted_operations == [{"date": "2023-09-15", "type": "EXECUTED"}]


    # def get_five_operations(self, sorted_operations: list[dict]) -> list[dict]:
    #     """
    #     получает последние 5 операций
    #     :return: список с последними 5 операциями в статусе "EXECUTED"
    #     """
    #     return sorted_operations[:5]

def test_get_five_operations():
    data_processor = DataProcessor('')
    assert data_processor.get_five_operations([]) == [] # мне нужна эта строчка? и без неё работает?
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