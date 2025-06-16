def get_mask_card_number(number_card: str) -> str:
    """Функция, возвращает маску для номера карты"""

    # Проверяем данные на корректность
    if len(number_card) == 16 and number_card.isdigit():
        begin_number_card: str = " ".join([number_card[:4], number_card[4:6]])
        new_number_card: str = " ** ** ** ".join([begin_number_card, number_card[-4:]])
        # функция возвращает номер карты ввиде: 7000 79** **** 6361
        return new_number_card

    else:

        return "Указан некорректный номер карты, повторите попытку"


def get_mask_account(number_account: str) -> str:
    """Функция, возвращает маску для номера счета"""

    # Проверяем данные на корректность
    if len(number_account) == 20 and number_account.isdigit():
        # функция возвращает номер счет ввиде: ** 4305
        return "**" + number_account[-4:]

    else:

        return "Указан некорректный номер счета, повторите попытку"
