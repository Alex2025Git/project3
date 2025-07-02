def filter_by_state(list_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED')
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """

    new_list_operation = []

    for operation in list_operation:
        if operation.get("state") == state:
            new_list_operation.append(operation)

    return new_list_operation


def sort_by_date(list_operation: list[dict], decreasing: bool = True) -> list:
    """
    Функция принимает список словарей и опционально значение для ключа decreasing (по умолчанию 'True')
    Возвращает новый отсортированный список словарей, в соотвествии с заданным
    ключом decreasing.
    """

    sorted_list_operation: list = sorted(
        list_operation, key=lambda x: x["date"], reverse=decreasing
    )

    return sorted_list_operation
