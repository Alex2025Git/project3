import json
import os
import logging
from src.external_api import external_transaction_amount

'''
1 - DEBUG — сообщения для отладки приложения.
2 - INFO — информационные сообщения.
3 - WARNING — предупреждения.
4 - ERROR — сообщения об ошибках.
5 - CRITICAL — критические сообщения.
'''
# Создаем логгер
logger = logging.getLogger(__name__)
# Задаем уровень
logger.setLevel(logging.DEBUG)
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler("../logs/utils.log", 'w', 'utf-8')
# Создаем формататер
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# Устанавлеваем форматер
file_handler.setFormatter(file_formatter)
# Устанавлеваем форматердобавляем хендлер
logger.addHandler(file_handler)


def read_json_files(path):
    logger.info(f'Запуск функции read_json_files с параметром "{path}"')
    try:
        if os.path.getsize(path) == 0:
            logger.error(f'Файл по указанному пути: "{path}", не найден!')
            return []
        else:
            with open(path, encoding="utf-8") as file:
                logger.info(f'Файл  "{path}", найден и открыт для чтения')
                list_data = json.load(file)
                if isinstance(list_data, list):
                    logger.info(f'Данные успешно считаны')
                    return list_data
                logger.error(f'Тип данных не сответсвует: "list"')
                return []
    except FileNotFoundError:
        logger.error(f'Файл не найден: "{path}"')
        return []


def transaction_amount(transaction):
    try:
        logger.info(f'Запуск функции transaction_amount с параметром "{transaction}"')

        operation_amount = transaction.get("operationAmount")
        logger.info(f'Данные получены "operation_amount": "{operation_amount}"')
        amount = operation_amount.get("amount")
        logger.info(f'Данные получены "amount": "{amount}"')
        code = operation_amount.get("currency").get("code")
        logger.info(f'Данные получены "code": "{code}"')

        if code == "RUB":
            logger.info(f'Возвращаем количество в RUB:"{float(amount)}"')
            return float(amount)

        logger.info(f'Обращение к сервису API конвертация "{float(amount)} {code}" в RUB')
        result = external_transaction_amount(amount, code)
        logger.info(f'Получен результат от API  {result}')
        return result

    except (AttributeError,UnboundLocalError) as err:
        logger.error(f'Ошибка: "{err}" в работе функции "transaction_amount"')
        return f'Ошибка {err}'
