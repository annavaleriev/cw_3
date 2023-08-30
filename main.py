from classes.data import DataProcessor
from settings import OPERATION_JSON


def main():
    data_processor = DataProcessor(OPERATION_JSON)
    all_operations = data_processor.get_operations_list()
    for operation in all_operations:
        print(operation)


if __name__ == '__main__':
    main()
