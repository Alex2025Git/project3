def filter_by_state(list_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, возвращает список операций по ключу"""

    new_list_operation = []

    for operation in list_operation:
        if operation.get("state") == state:
            new_list_operation.append(operation)

    return new_list_operation
