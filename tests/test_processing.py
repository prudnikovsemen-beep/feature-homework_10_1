import unittest
from src.processing import filter_by_state, sort_by_date

class TestProcessingFunctions(unittest.TestCase):
    def setUp(self):
        """Подготавливаем тестовые данные."""
        self.operations = [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

    def test_filter_by_state_default(self):
        """Тест фильтрации по умолчанию (EXECUTED)."""
        result = filter_by_state(self.operations)
        self.assertEqual(len(result), 2)
        for op in result:
            self.assertEqual(op["state"], "EXECUTED")

    def test_filter_by_state_cancelled(self):
        """Тест фильтрации по статусу CANCELLED."""
        result = filter_by_state(self.operations, "CANCELED")
        self.assertEqual(len(result), 2)
        for op in result:
            self.assertEqual(op["state"], "CANCELED")

    def test_sort_by_date_descending(self):
        """Тест сортировки по убыванию (самые последние сначала)."""
        result = sort_by_date(self.operations)
        dates = [op["date"] for op in result]
        # Проверяем, что даты идут в порядке убывания
        self.assertTrue(dates[0] > dates[1] > dates[2] > dates[3])

    def test_sort_by_date_ascending(self):
        """Тест сортировки по возрастанию."""
        result = sort_by_date(self.operations, reverse=False)
        dates = [op["date"] for op in result]
        # Проверяем, что даты идут в порядке возрастания
        self.assertTrue(dates[0] < dates[1] < dates[2] < dates[3])


if __name__ == "__main__":
    unittest.main()
