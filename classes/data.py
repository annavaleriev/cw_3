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
    def get_executed_operations(self, list_operations) -> list:
        """
        достает операции "EXECUTED" и добавляет их в список
        :return: список операций выполненных со статусом "EXECUTED"
        """
        # executed_list = []
        # for operation in list_operation:
        #     if operation["state"] == "EXECUTED":
        #         executed_list.append(operation)
        return [operation for operation in list_operations if operation.get("state") == "EXECUTED"]

    def sort_operations(self, executed_operations) -> list:
        """
         сортирует список операций по дате
        :return: список операций "EXECUTED" отсортированный с конца
        """
        return sorted(executed_operations, key=lambda operation: operation["date"], reverse=True)

    def get_five_operations(self, sorted_operations) -> list: # или тут словарь?
        """
        получает последние 5 операций
        :return: список с последними 5 операциями в статусе "EXECUTED"
        """
        return sorted_operations[:5]

    def get_operation_objects(self, five_operations):
        """
        берёт 5 операций
        :param five_operations:
        :return: возаращает 5 экземпляров класса
        """
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
            operation_object = Operation(operation_dict.keys())
            if operation_object.state == "EXECUTED":
                list_objects.append(operation_object)
        return list_objects


    def get_operations_list(self):
        list_operations = self.load_data()
        executed_operations = self.get_executed_operations(list_operations)
        sorted_operations = self.sort_operations(executed_operations)
        five_operations = self.get_five_operations(sorted_operations)
        all_operations = self.get_operation_objects(five_operations)
        pass




# data_proc = DataProcessor(OPERATION_JSON)
# print(data_proc.get_operation_objects())

