import logging

# Создаем логгер
logger = logging.getLogger(__name__)
# Задаем уровень
logger.setLevel(logging.DEBUG)
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler("../logs/masks.log", "w", "utf-8")
# Создаем формататер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
# Устанавлеваем форматер
file_handler.setFormatter(file_formatter)
# Устанавлеваем форматердобавляем хендлер
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """
    Функция принимает строку,
    Возвращает новую строку, в соответсвии с маской номера карты XXXX XX** **** XXXX
    """
    # Проверяем данные на корректность
    logger.info(f'Запуск функции get_mask_card_number с параметром: "{number_card}"')
    if (
        isinstance(number_card, str)
        and len(number_card) == 16
        and number_card.isdigit()
    ):
        begin_number_card: str = " ".join([number_card[:4], number_card[4:6]])
        new_number_card: str = " ** ** ** ".join([begin_number_card, number_card[-4:]])
        # функция возвращает номер карты ввиде: XXXX XX** **** XXXX
        logger.info(f'Номер карты успешно преобразован: "{new_number_card}"')
        return new_number_card

    else:
        logger.error(
            f'Указан некорректный номер карты: "{number_card}", преобразование не возможно'
        )
        return "Указан некорректный номер карты, повторите попытку"


def get_mask_account(number_account: str) -> str:
    """
    Функция принимает строку, длина которой равна 20 и состоит из чисел
    Возвращает новую строку, в соответсвии с маской номера счета ** XXXX
    """
    # Проверяем данные на корректность
    logger.info(f'Запуск функции get_mask_account с параметром "{number_account}"')
    if (
        isinstance(number_account, str)
        and len(number_account) == 20
        and number_account.isdigit()
    ):
        # функция возвращает номер счет ввиде: ** XXXX
        logger.info(f'Номер карты успешно преобразован: "{"**" + number_account[-4:]}"')
        return "**" + number_account[-4:]

    else:
        logger.error(
            f'Указан некорректный номер счета: "{number_account}", преобразование не возможно'
        )
        return "Указан некорректный номер счета, повторите попытку"
