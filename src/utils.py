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

    amount = operation_amount.get("amount")
    code = operation_amount.get("currency").get("code")

    if code == "RUB":
        return float(amount)

    result = external_transaction_amount(amount, code)

    return result
