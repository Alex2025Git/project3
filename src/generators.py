from typing import Any, Generator


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Generator[dict, Any, None]:
    """
    Функция - генератор, которая принимает список словарей с транзакциями
    Возвращает операциию, где валюта соответствует заданной.
    """
    for i in transactions:
        if get_operationAmount := i.get("operationAmount"):
            if get_currency := get_operationAmount.get("currency"):
                if get_currency.get("code") == currency:
                    yield i


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, Any, None]:
    """
    Функция - генератор, которая принимает список словарей с транзакциями
    Возвращает описание каждой операции по очереди.
    """
    for i in transactions:
        if description := i.get("description"):
            yield description


def card_number_generator(start: str, stop: str) -> Generator[str, Any, None]:
    """
    Функция - генератор, которая принимает на вход диапозон от '0000000000000000' до '9999999999999999'
    Возвращает номер карты соотвествующий маске: XXXX XXXX XXXX XXXX
    """
    if (
        isinstance(start, str)
        and start.isdigit()
        and 0 < int(start) <= 9999999999999999
        and isinstance(stop, str)
        and stop.isdigit()
        and 0 < int(stop) <= 9999999999999999
        and int(stop) >= int(start)
        and len(start) == 16
        and len(stop) == 16
    ):
        int_number_begin = int(start)
        int_number_end = int(stop)
        for i in range(int_number_begin, int_number_end + 1):
            number_mask = f"{i:0{16}}"
            number_card = " ".join([number_mask[i - 4 : i] for i in range(4, 20, 4)])
            yield number_card
    else:
        yield "Указаны некорректные данные"
