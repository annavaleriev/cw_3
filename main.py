from classes.data import DataProcessor
from classes.operation import Operation
from settings import OPERATION_JSON


def main() -> None:
    data_processor: DataProcessor = DataProcessor(OPERATION_JSON)
    all_operations: list[Operation] = data_processor.get_operations_list()
    for operation in all_operations:
        print(operation)


if __name__ == '__main__':
    main()
