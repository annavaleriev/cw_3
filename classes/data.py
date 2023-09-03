import json

from classes.operation import Operation


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
        with open(self.path, encoding="utf-8") as data_file:
            return json.load(data_file)


class DataProcessor(Data):
    def get_executed_operations(self, list_operations: list[dict]) -> list[dict]:
        """
        достает операции "EXECUTED" и добавляет их в список
        :return: список операций выполненных со статусом "EXECUTED"
        """
        return [operation for operation in list_operations if operation.get("state") == "EXECUTED"]

    def sort_operations(self, executed_operations: list[dict]) -> list[dict]:
        """
         сортирует список операций по дате
        :return: список операций "EXECUTED" отсортированный с конца
        """
        return sorted(executed_operations, key=lambda operation: operation["date"], reverse=True)

    def get_five_operations(self, sorted_operations: list[dict]) -> list[dict]:
        """
        получает последние 5 операций
        :return: список с последними 5 операциями в статусе "EXECUTED"
        """
        return sorted_operations[:5]

    def get_operation_objects(self, five_operations: list[dict]) -> list[Operation]:
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
                "from_": operation.get("from", ""),
                "to": operation["to"]

            }
            list_objects.append(Operation(**operation_dict))
        return list_objects

    def get_operations_list(self) -> list[Operation]:
        list_operations: list[dict] = self.load_data()
        executed_operations: list[dict] = self.get_executed_operations(list_operations)
        sorted_operations: list[dict] = self.sort_operations(executed_operations)
        five_operations: list[dict] = self.get_five_operations(sorted_operations)
        all_operations: list[Operation] = self.get_operation_objects(five_operations)
        return all_operations
