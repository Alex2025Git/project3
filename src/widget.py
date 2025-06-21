from datetime import datetime


def mask_account_card(bank_details: str) -> str:
    """
    Функция принимает строку,
    Возвращает новую строку, в соответсвии с маской номера карты XXXX XX** **** XXXX
    или номера счета **XXXX
    """
    if type(bank_details) == str and len(bank_details) > 0:
        list_details: list = bank_details.split()
        account_card: str = list_details[-1]
        if len(account_card) == 16 and account_card.isdigit():
            begin_number_card: str = " ".join([account_card[:4], account_card[4:6]])
            list_details[-1] = " ** ** ** ".join([begin_number_card, account_card[-4:]])
            number_card: str = " ".join(list_details)

            # функция возвращает номер карты ввиде: 7000 79** **** 6361
            return number_card

        elif len(account_card) == 20 and account_card.isdigit():

            list_details[-1] = "**" + account_card[-4:]
            number_account: str = " ".join(list_details)

            # функция возвращает номер счет ввиде: ** 4305
            return number_account

        else:

            return "Указан некорректный номер карты, повторите попытку"

    return "Указан некорректный номер карты, повторите попытку"


def get_date(srt_date: str) -> str:
    """Функция, возвращает из строки дату в формате ДД.ММ.ГГГГ"""
    """
    Функция принимает строку,
    Возвращает новую строку в формате ДД.ММ.ГГГГ
    """
    try:
        # преобразуем строку в дату
        format_date = datetime.strptime(srt_date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return "Указан некорректный формат даты, повторите попытку"
    except TypeError:
        return "Указан некорректный формат даты, повторите попытку"
    # возвращаем необходимый формат "ДД.ММ.ГГГГ"
    return format_date.strftime("%d.%m.%Y")
