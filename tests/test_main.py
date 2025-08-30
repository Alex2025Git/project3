from unittest import TestCase
from unittest.mock import patch

from src.main import main


class MyTest(TestCase):

    @patch("builtins.input")
    def test_main(self, mock_get1):
        # Здесь ты можешь настроить поведение замоканных функций

        mock_get1.side_effect = [
            "1",
            "EXECUTED",
            "Да",
            "по возрастанию",
            "Да",
            "Да" "Перевод",
        ]
        # Вызов тестируемой функции
        result = main()

        # Проверка результата
        self.assertEqual(result, None)

        # Проверка, что замоканные функции были вызваны
        mock_get1.assert_called()
