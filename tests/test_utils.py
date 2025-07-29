from unittest.mock import patch

from src.external_api import external_transaction_amount
from src.utils import read_json_files, transaction_amount


@patch("requests.get")
def test_external_transaction_amount(mock_get):
    mock_get.return_value.json.return_value = {"code": "USD", "amount": "1"}
    assert external_transaction_amount("1", "USD") == {"code": "USD", "amount": "1"}
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "3S7N6kt2xKdnHAkF2BJtX4NrlR4XZlTb"},
        params={"amount": "1", "from": "USD", "to": "RUB"},
    )


def test_transaction_amount(example_list_number_card):
    assert (
        transaction_amount({"test": "1"})
        == 'Некорректная транзацкия отсутствует "operationAmount"'
    )
    assert transaction_amount(example_list_number_card[4]) == 67314.70


def test_read_json_files():
    assert read_json_files("") == []
    assert type(read_json_files("../date/operations.json")) == list
