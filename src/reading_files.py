import csv

import pandas as pd


def reading_transactions_csv(path: str) -> list:
    """
    Функция для работы с CSV принимает путь к файлу в качестве аргумента
    Возвращает список словарей с транзакциями.
    """

    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        new_list = []
        for row in reader:
            new_list.append(row)
        return new_list


def reading_transactions_excel(path: str) -> list:
    """
    Функция для работы с XLSX принимает путь к файлу в качестве аргумента
    Возвращает список словарей с транзакциями.
    """

    excel_data = pd.read_excel(path)
    list_transaction = excel_data.to_dict(orient="records")
    return list_transaction
