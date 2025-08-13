from unittest.mock import patch

import pandas as pd

from src.reading_files import reading_transactions_csv as read_csv
from src.reading_files import reading_transactions_excel as read_excel


@patch("csv.DictReader")
def test_reading_transactions_csv(mock_get, example_list_number_card):
    mock_get.return_value = example_list_number_card
    assert read_csv('C:\\Users\HomePC\project3\date\\transactions.csv') == example_list_number_card


@patch("pandas.read_excel")
def test_reading_transactions_excel(mock_get, example_list_number_card):
    test = pd.DataFrame(example_list_number_card)
    mock_get.return_value = test
    assert read_excel("../date/transactions_excel.xlsx") == example_list_number_card
