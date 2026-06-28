import unittest
from src.widget import get_date

class TestWidgetFunctions(unittest.TestCase):
    def test_get_date_valid(self):
        """Тест корректного преобразования даты."""
        input_date = "2024-03-11T02:26:18.671407"
        expected = "11.03.2024"
        result = get_date(input_date)
        self.assertEqual(result, expected)

    def test_get_date_edge_cases(self):
        """Тест крайних случаев для преобразования даты."""
        test_cases = [
            ("2000-01-01T00:00:00", "01.01.2000"),
            ("2099-12-31T23:59:59.999999", "31.12.2099"),
        ]
        for input_date, expected in test_cases:
            with self.subTest(input_date=input_date):
                result = get_date(input_date)
                self.assertEqual(result, expected)
