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


def card_number_generator(
    number_begin: str, number_end: str
) -> Generator[str, Any, None]:
    """
    Функция - генератор, которая принимает на вход диапозон от '0000000000000000' до '9999999999999999'
    Возвращает номер карты соотвествующий маске: XXXX XXXX XXXX XXXX
    """
    if (
        isinstance(number_begin, str)
        and number_begin.isdigit()
        and 0 < int(number_begin) <= 9999999999999999
        and isinstance(number_end, str)
        and number_end.isdigit()
        and 0 < int(number_end) <= 9999999999999999
        and int(number_end) >= int(number_begin)
        and len(number_begin) == 16
        and len(number_end) == 16
    ):
        int_number_begin = int(number_begin)
        int_number_end = int(number_end)
        for i in range(int_number_begin, int_number_end + 1):
            number_mask = f"{i:0{16}}"
            number_card = " ".join([number_mask[i - 4: i] for i in range(4, 20, 4)])
            yield number_card
    else:
        yield "Указаны некорректные данные"
