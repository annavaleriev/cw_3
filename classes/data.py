import json

from classes.operation import Operation
from settings import OPERATION_JSON


class Data:
    def __init__(self, path: str):
        """
        инициализация класса
        :param path: путь к файлу
        """
        self.path = path

    def load_data(self) -> list[dict]:
        """
        считывает файл по указанному пути
        :return: список словарей
        """
        with open(self.path) as data_file:
            return json.load(data_file)

# data = Data(OPERATION_JSON)
# print(data.load_data())

class DataProcessor(Data):
    def get_executed_operations(self, list_operations):
        # executed_list = []
        # for operation in list_operation:
        #     if operation["state"] == "EXECUTED":
        #         executed_list.append(operation)
        return [operation for operation in list_operations if operation.get("state") == "EXECUTED"]

    def sort_operations(self, executed_operations):
        return sorted(executed_operations, key=lambda operation: operation["date"], reverse=True)

    def get_five_operations(self, sorted_operations):
        return sorted_operations[:5]

    def get_operation_objects(self, five_operations):
        list_objects = []
        for operation in five_operations:
            operation_dict = {
                "pk": operation["id"],
                "date": operation["date"],
                "state": operation["state"],
                "operation_amount": operation["operationAmount"],
                "description": operation["description"],
                "from_": operation["from"],
                "to": operation["to"]

            }




    def get_operations_list(self):
        list_operations = self.load_data()
        executed_operations = self.get_executed_operations(list_operations)
        sorted_operations = self.sort_operations(executed_operations)
        five_operations = self.get_five_operations(sorted_operations)






data_proc = DataProcessor(OPERATION_JSON)
print(data_proc.get_executed_operations())

