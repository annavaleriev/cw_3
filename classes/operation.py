from datetime import datetime


class Operation:
    def __init__(self, pk: int, date: str, state: str, operation_amount: dict, description: str, from_: str, to: str):
        """
        инициализауия класса
        :param pk:
        :param date:
        :param state:
        :param operation_amount:
        :param description:
        :param from_:
        :param to:
        """
        self.pk = pk
        self.date = self.convert_date(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.hide_card_number(from_) if from_ else ""
        self.to = self.hide_card_number(to)

    def convert_date(self, date: str) -> str:
        """
        форматирование даты
        :param date:
        :return:
        """
        correct_date = datetime.fromisoformat(date) #какой тут тип и что возвращает
        return correct_date.strftime('%d.%m.%Y')

    def hide_card_number(self, card: str) -> str:
        """
        счёт или номер карты маскирует перед выводом
        :param card:
        :return:
        """
        if card.startswith('Счет'):
            return f'Счет ** {card[-4:]}'
        else:
            card_split: list[str] = card.split()
            card_number: str = card_split.pop()
            card_number: str = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
            card_split.append(card_number)
            return " ".join(card_split)

    def __str__(self) -> str:
        """
        выводит сообщение по операции
        :return: строку с данными по операции
        """
        return (f'{self.date} {self.description}\n'
                f'{self.from_} -> {self.to}\n '
                f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}')
