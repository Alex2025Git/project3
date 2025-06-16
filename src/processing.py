def filter_by_state(list_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, возвращает список операций по ключу"""

    new_list_operation = []

    for operation in list_operation:
        if operation.get("state") == state:
            new_list_operation.append(operation)

    return new_list_operation


def sort_by_date(list_operation: list[dict], decreasing: bool = True) -> list:
    """Функция, возвращает отсортированный по дате список операций"""

    sorted_list_operation: list = sorted(
        list_operation, key=lambda x: x["date"], reverse=decreasing
    )

    return sorted_list_operation
