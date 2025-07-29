import json
import os

from src.external_api import external_transaction_amount


def read_json_files(path):
    try:
        if os.path.getsize(path) == 0:
            return []
        else:
            with open(path, encoding="utf-8") as file:
                list_data = json.load(file)
                if isinstance(list_data, list):
                    return list_data
                return []
    except FileNotFoundError:
        return []


def transaction_amount(transaction):
    operation_amount = transaction.get("operationAmount")

    if operation_amount is None:
        return 'Некорректная транзацкия отсутствует "operationAmount"'
    else:

        amount = operation_amount.get("amount")
        if amount is None:
            return 'Некорректная транзацкия отсутствует "amount"'

        currency = operation_amount.get("currency")
        if currency is None:
            return 'Некорректная транзацкия отсутствует "currency"'
        else:
            code = currency.get("code")
            if code is None:
                return 'Некорректная транзацкия отсутствует "code"'

    if code == "RUB":
        return float(amount)
    else:
        result = external_transaction_amount(amount, code)
    return result
