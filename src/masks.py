def get_mask_card_number(number_card: str) -> str:
    """
    Функция принимает строку,
    Возвращает новую строку, в соответсвии с маской номера карты XXXX XX** **** XXXX
    """
    # Проверяем данные на корректность
    if type(number_card) == str and len(number_card) == 16 and number_card.isdigit():
        begin_number_card: str = " ".join([number_card[:4], number_card[4:6]])
        new_number_card: str = " ** ** ** ".join([begin_number_card, number_card[-4:]])
        # функция возвращает номер карты ввиде: XXXX XX** **** XXXX
        return new_number_card

    else:

        return "Указан некорректный номер карты, повторите попытку"


def get_mask_account(number_account: str) -> str:
    """
    Функция принимает строку, длина которой равна 20 и состоит из чисел
    Возвращает новую строку, в соответсвии с маской номера счета ** XXXX
    """
    # Проверяем данные на корректность
    if (
        type(number_account) == str
        and len(number_account) == 20
        and number_account.isdigit()
    ):
        # функция возвращает номер счет ввиде: ** XXXX
        return "**" + number_account[-4:]

    else:

        return "Указан некорректный номер счета, повторите попытку"
