from src.generators import filter_by_currency
from src.processing import filter_by_state as fl_status
from src.processing import process_bank_search as pr_search
from src.processing import sort_by_date as sr_date
from src.reading_files import reading_transactions_csv as rd_csv
from src.reading_files import reading_transactions_excel as rd_excel
from src.utils import read_json_files as rd_json
from src.widget import get_date, mask_account_card


def main():
    get_menu = {
        1: "Получить информацию о транзакциях из файла JSON-файла",
        2: "Получить информацию о транзакциях из файла CSV-файла",
        3: "Получить информацию о транзакциях из файла XLSX-файла",
    }

    get_names_def = {
        1: rd_json("C:/Users/HomePC/project3/date/operations.json"),
        2: rd_csv("C:/Users/HomePC/project3/date/transactions.csv"),
        3: rd_excel("C:/Users/HomePC/project3/date/transactions_excel.xlsx"),
    }

    answer_input = {
        1: "Для обработки выбран JSON-файл.",
        2: "Для обработки выбран CSV-файл.",
        3: "Для обработки выбран XLSX-файл.",
    }

    status = ["EXECUTED", "CANCELED", "PENDING"]

    print(
        "Привет! Добро пожаловать в программу работы \nс банковскими транзакциями"
        "\nВыбирите необходимый пункт меню:"
    )
    for i, k in get_menu.items():
        print(f"{i}. {k}")

    while True:
        menu_item = input("\nВвод данных: ")
        if menu_item.isdigit() and answer_input.get(int(menu_item)) is not None:
            list_dict = get_names_def[int(menu_item)]
            print(f"\n{answer_input[int(menu_item)]}")
            break
        else:
            print(f"\nВыборанный пункт меню {menu_item} недоступен, повторите попытку")

    srt_status = ", ".join(status)
    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {srt_status}"
        )
        input_user = input("\nВвод данных: ")
        if input_user.isalpha() and input_user.upper() in status:
            fl_list_dict = fl_status(list_dict, input_user.upper())
            print(f'\nОперации отфильтрованы по статусу "{input_user.upper()}"')
            break
        else:
            print(f"\nСтатус операции {input_user} недоступен.")

    print("\nОтсортировать операции по дате?")
    input_user = input('\nВведите "Да" или "Нет": ')
    if input_user.isalpha() and input_user.upper() in "ДА":
        print("\nОтсортировать по возрастанию или по убыванию?")
        input_user = input('\nВведите "по возрастанию" или "по убыванию": ')
        if input_user.isalpha() and input_user.lower() in [
            "по возрастанию",
            "по убыванию",
        ]:
            fl_list_dict = sr_date(fl_list_dict, input_user.lower() == "по убыванию")

    print("\nВыводить только рублевые транзакции?")
    input_user = input('\nВведите "Да" или "Нет": ')
    if input_user.isalpha() and input_user.upper() in "ДА":
        generator_value = filter_by_currency(fl_list_dict, "RUB")
        new_list = []
        while True:
            try:
                new_list.append(next(generator_value))
            except StopIteration:
                fl_list_dict = new_list
                break

    print("\nОтфильтровать список транзакций по определенному слову в описании?")
    input_user = input('\nВведите "Да" или "Нет": ')
    if input_user.isalpha() and input_user.upper() == "ДА":
        find_description = input("\nУкажите, слово для поиска: ")
        fl_list_dict = pr_search(fl_list_dict, find_description)

    count_operation = len(fl_list_dict)
    if count_operation == 0:
        print(
            "\nНе найдено ни одной транзакции, подходящей под ваши \nусловия фильтрации"
        )
    else:
        print("\nРаспечатываю итоговый список транзакций...")

        print(f"\nВсего банковских операций в выборке:{count_operation}")

        for i in fl_list_dict:
            description = i.get("description")
            date_operation = f'{get_date(i.get("date"))} {description}'
            mask_to = i.get("to").split()
            mask_account_to = (
                f'{" ".join(mask_to[:-1])} {mask_account_card(mask_to[-1])}'
            )
            operation_amount = i.get("operationAmount")
            amount = operation_amount.get("amount")
            code = operation_amount.get("currency").get("name")

            if description == "Открытие вклада":
                print(f"\n{date_operation} \n{mask_account_to} \nСумма: {amount} {code}")
            else:
                mask_from = i.get("from").split()
                mask_account_from = (
                    f'{" ".join(mask_from[:-1])} {mask_account_card(mask_from[-1])}'
                )
                print(
                    f"\n{date_operation} \n{mask_account_from} -> {mask_account_to} \nСумма: {amount} {code}"
                )
