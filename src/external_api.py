import os

import requests
from dotenv import load_dotenv


def external_transaction_amount(amount, code):

    # Загрузка переменных из .env-файла
    load_dotenv()
    # Получение значения переменной API_KEY из .env-файла
    token = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {"amount": amount, "from": code, "to": "RUB"}
    headers = {"apikey": f"{token}"}
    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code
    result = response.json()
    if status_code == 200:
        get_result = result.get("result")
        return float(get_result)
    return result
