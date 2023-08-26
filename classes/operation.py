from datetime import datetime



class Operation:
    def __init__(self, pk: int, date: str, state: str, operation_amount: dict, description: str, from_: str, to: str):
        self.pk = pk
        self.date = self.convert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.hide_card_number(from_) if from_ else ""
        self.to = self.hide_card_number(to)

    def convert_date(self, date):
        correct_date = datetime.fromisoformat(date)
        return correct_date.strftime('%d.%m.%Y')

    def hide_card_number(self, card: str):
        if card.startswith('Счет'):
            return f'Счет ** {card[-4:]}'
        else:
            card_split: list[str] = card.split()
            card_number: str = card_split.pop()
            card_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
            card_split.append(card_number)
            return " ".join(card_split)

    def print_operation(self):
        return (f'{self.date} {self.description}\n'
                f'{self.from_} -> {self.to}\n '
                f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}')



    # def last_five_operations(self, date):
    #
    #     for
    #



# oper = Operation (12345,'2019-08-26T10:50:58.294041', "EXECUTED", {
#       "amount": "123.58",
#       "currency": {
#         "name": "USD",
#         "code": "RUB"
#       }}, "Перевод организации",'Maestro 1596837868705199', 'Счет 35383033474447895560')
# # print(oper.date)
# # print(oper.from_)
# # print(oper.to)
#
#
# # print(oper.operation_amount)
# print(oper.print_operation())

# print(oper.last_five_operations())


#
# class DataConnector:
#     def __init__(self, data):
#         self.data = data
#         correct_date = datetime.fromisoformat(self.data['date'])
#         date_ = correct_date.strftime('%d.%m.%Y')
#         return date_






    # data = Data(OPERATION_JSON)
    # вот этот надо передать туда экземпляер класса




