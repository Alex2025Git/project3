import pytest

from src import masks

error_get_mask_account = "Указан некорректный номер счета, повторите попытку"
error_get_mask_card_number = "Указан некорректный номер карты, повторите попытку"


# вызываем тест-функцию для проверки получения маски номера карты
@pytest.mark.parametrize(
    "value, expected",
    [
        ("", error_get_mask_card_number),
        ("1234567891234567", "1234 56 ** ** ** 4567"),
        ("12323455", error_get_mask_card_number),
        (0, error_get_mask_card_number),
        ("12345678*-1234567", error_get_mask_card_number),
    ],
)
def test_get_mask_card_number(value, expected):
    assert masks.get_mask_card_number(value) == expected


# вызываем тест-функцию для проверки получения маски счета
@pytest.mark.parametrize(
    "value, expected",
    [
        ("", error_get_mask_account),
        ("12345678912345678912", "**8912"),
        ("12323455", error_get_mask_account),
        (10, error_get_mask_account),
        ("12345678*-1234567", error_get_mask_account),
    ],
)
def test_get_mask_account(value, expected):
    assert masks.get_mask_account(value) == expected
