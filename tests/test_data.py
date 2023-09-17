from classes.data import DataProcessor


def test_get_executed_operations():
    data_processor = DataProcessor('')
    assert data_processor.get_executed_operations([{"state": "EXECUTED", "id": 1}, {"state": "CANCELED", "id": 2}]) == [
        {"state": "EXECUTED", "id": 1}]
    assert data_processor.get_executed_operations([]) == []
    assert data_processor.get_executed_operations([{"id": 1}, {"id": 2}]) == []


def test_sort_operations():
    data_processor = DataProcessor('')
    assert data_processor.sort_operations([]) == []
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


