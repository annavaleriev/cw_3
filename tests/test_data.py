from classes.data import DataProcessor
from tests.conftest import executed_operations, sorted_operations, last_five__operations


def test_get_executed_operations(test_json, executed_operations):
    test_get_executed_operations = DataProcessor(test_json)
    # assert DataProcessor.get_executed_operations(test_get_executed_operations, test_json) == []
    assert DataProcessor.get_executed_operations(test_get_executed_operations, test_json) == executed_operations


def test_sort_operations(executed_operations, sorted_operations):
    test_get_executed_operations = DataProcessor(executed_operations)
    assert DataProcessor.sort_operations(test_get_executed_operations, executed_operations) == sorted_operations


def test_get_five_operations(sorted_operations, last_five__operations):
    test_get_executed_operations = DataProcessor(sorted_operations)
    assert DataProcessor.get_five_operations(test_get_executed_operations, sorted_operations) == last_five__operations



