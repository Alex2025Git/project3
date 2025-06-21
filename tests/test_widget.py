import pytest

from src import widget

# вызываем тест-функцию для проверки получения маски счета и карты
error_get_mask_card_number = 'Указан некорректный номер карты, повторите попытку'
@pytest.mark.parametrize('value, expected',[('', error_get_mask_card_number),
                                            ('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79 ** ** ** 6361'),
                                            ('Счет 73654108430135874305', 'Счет **4305'),
                                            (12323455, error_get_mask_card_number),
                                            ('12345678*-1234567', error_get_mask_card_number)])

def test_get_mask_card_number(value, expected):
    assert widget.mask_account_card(value) == expected

# вызываем тест-функцию для проверки получения даты из строки в формате "ДД.ММ.ГГГГ"
error_get_date = 'Указан некорректный формат даты, повторите попытку'
@pytest.mark.parametrize('value, expected',[('', error_get_date),
                                            ('2024-03-11T02:26:18.671407', '11.03.2024'),
                                            ('11.03.2024', error_get_date),
                                            (21062025, error_get_date),
                                            ('20250621', error_get_date)])

def test_get_date(value, expected):
    assert widget.get_date(value) == expected