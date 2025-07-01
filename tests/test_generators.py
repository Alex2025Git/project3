import pytest

from src import generators


# вызываем тест-функцию для проверки получения маски номера карты
@pytest.mark.parametrize(
    "number_begin, number_end, expected",
    [
        ("", "", 'Указаны некорректные данные'),
        (0, "", 'Указаны некорректные данные'),
        (" ", " ", 'Указаны некорректные данные'),
        ("0000000000000008", "0000000000000011", '0000 0000 0000 0008'),
        (8, 11, 'Указаны некорректные данные'),
    ],
)
def test_card_number_generator(number_begin, number_end, expected):
    get_mask_card_number = generators.card_number_generator(number_begin, number_end)
    assert next(get_mask_card_number) == expected


# вызываем тест-функцию для проверки получения маски номера карты 2 вариант
@pytest.mark.parametrize(
    "num_beg, num_end, expected",
    [
        ("0000000000000001", "0000000000000003",["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"])
    ],
)
def test_card_number_generator_two(num_beg, num_end, expected):
    get_mask_card_number = generators.card_number_generator(num_beg, num_end)
    assert next (get_mask_card_number) == expected[0]
    assert next (get_mask_card_number) == expected[1]
    assert next (get_mask_card_number) == expected[2]


# вызываем тест-функцию для проверки получения операции по указанной валюте
def test_filter_by_currency(example_list_number_card, list_number_card_answer):
        try:
            usd_transactions = generators.filter_by_currency(example_list_number_card, "USD")
            assert (next(usd_transactions)) == list_number_card_answer[0]
            assert (next(usd_transactions)) == list_number_card_answer[1]
            assert (next(usd_transactions)) == list_number_card_answer[2]
        except StopIteration:
            print('Нет данных')


# вызываем тест-функцию для проверки получения описания операций
def test_transaction_descriptions(example_list_number_card, list_description):
    try:
        usd_transactions = generators.transaction_descriptions(example_list_number_card)
        assert (next(usd_transactions)) == list_description[0]
        assert (next(usd_transactions)) == list_description[1]
        assert (next(usd_transactions)) == list_description[2]
        assert (next(usd_transactions)) == list_description[3]
        assert (next(usd_transactions)) == list_description[4]
    except StopIteration:
        print('Нет данных')
