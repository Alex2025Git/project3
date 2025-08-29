import csv

import pandas as pd


def reading_transactions_csv(path: str) -> list:
    """
    Функция для работы с CSV принимает путь к файлу в качестве аргумента
    Возвращает список словарей с транзакциями.
    """

    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        new_list = [normalize_transaction(transaction) for transaction in reader]

        return new_list


def reading_transactions_excel(path: str) -> list:
    """
    Функция для работы с XLSX принимает путь к файлу в качестве аргумента
    Возвращает список словарей с транзакциями.
    """

    excel_data = pd.read_excel(path)
    list_transactions = excel_data.to_dict(orient="records")
    new_list = [normalize_transaction(transaction) for transaction in list_transactions]

    return new_list


def normalize_transaction(transaction):
    """Функция принимает в качестве аргумента словарь с данными по транзакции и
    возвращаетя нормализованные данные"""

    if "operationAmount" not in transaction:
        transaction["operationAmount"] = {
            "amount": transaction.pop("amount"),
            "currency": {
                "name": transaction.pop("currency_name"),
                "code": transaction.pop("currency_code"),
            },
        }

    return transaction
