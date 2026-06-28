import unittest
from src.masks import get_mask_card_number, get_mask_account

class TestMasksFunctions(unittest.TestCase):
    """Тесты для функций маскировки номеров карт и счетов."""

    def test_get_mask_card_number_valid(self):
        """Тест корректной маскировки номера карты."""
        # Тестовые данные: (входной номер, ожидаемый результат)
        test_cases = [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("9999888877776666", "9999 88** **** 6666"),
        ]

        for card_number, expected in test_cases:
            with self.subTest(card_number=card_number):
                result = get_mask_card_number(card_number)
                self.assertEqual(result, expected)

    def test_get_mask_card_number_with_spaces(self):
        """Тест маскировки номера карты с пробелами."""
        input_card = "7000 7922 8960 6361"
        expected = "7000 79** **** 6361"
        result = get_mask_card_number(input_card)
        self.assertEqual(result, expected)

    def test_get_mask_card_number_invalid_length(self):
        """Тест обработки номера карты неверной длины."""
        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")  # 15 цифр

        with self.assertRaises(ValueError):
            get_mask_card_number("12345678901234567")  # 17 цифр

    def test_get_mask_card_number_non_numeric(self):
        """Тест обработки нечислового номера карты."""
        with self.assertRaises(ValueError):
            get_mask_card_number("abcdefghijklmnop")

        with self.assertRaises(ValueError):
            get_mask_card_number("7000a922b960c361")

    def test_get_mask_account_valid(self):
        """Тест корректной маскировки номера счёта."""
        # Тестовые данные: (входной номер, ожидаемый результат)
        test_cases = [
            ("73654108430135874305", "**4305"),
            ("1234567890", "**90"),
            ("00000000000000000001", "**0001"),
            ("99999999999999999999", "**9999"),
        ]

        for account_number, expected in test_cases:
            with self.subTest(account_number=account_number):
                result = get_mask_account(account_number)
                self.assertEqual(result, expected)

    def test_get_mask_account_with_spaces(self):
        """Тест маскировки номера счёта с пробелами."""
        input_account = "7365 4108 4301 3587 4305"
        expected = "**4305"
        result = get_mask_account(input_account)
        self.assertEqual(result, expected)

    def test_get_mask_account_non_numeric(self):
        """Тест обработки нечислового номера счёта."""
        with self.assertRaises(ValueError):
            get_mask_account("abcdefghij")

        with self.assertRaises(ValueError):
            get_mask_account("7365a108b430c358d430e")

    def test_get_mask_account_empty(self):
        """Тест обработки пустого номера счёта."""
        with self.assertRaises(ValueError):
            get_mask_account("")

    def test_get_mask_account_short(self):
        """Тест обработки короткого номера счёта (менее 4 цифр)."""
        test_cases = ["1", "12", "123"]
        expected_results = ["**1", "**12", "**123"]

        for account, expected in zip(test_cases, expected_results):
            with self.subTest(account=account):
                result = get_mask_account(account)
                self.assertEqual(result, expected)

import unittest
from src.masks import get_mask_card_number, get_mask_account



class TestMasksFunctions(unittest.TestCase):
    """Тесты для функций маскировки номеров карт и счетов."""

    def test_get_mask_card_number_valid(self):
        """Тест корректной маскировки номера карты."""
        # Тестовые данные: (входной номер, ожидаемый результат)
        test_cases = [
            ("7000792289606361", "7000 79** **** 6361"),
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("9999888877776666", "9999 88** **** 6666"),
        ]

        for card_number, expected in test_cases:
            with self.subTest(card_number=card_number):
                result = get_mask_card_number(card_number)
                self.assertEqual(result, expected)

    def test_get_mask_card_number_with_spaces(self):
        """Тест маскировки номера карты с пробелами."""
        input_card = "7000 7922 8960 6361"
        expected = "7000 79** **** 6361"
        result = get_mask_card_number(input_card)
        self.assertEqual(result, expected)

    def test_get_mask_card_number_invalid_length(self):
        """Тест обработки номера карты неверной длины."""
        with self.assertRaises(ValueError):
            get_mask_card_number("123456789012345")  # 15 цифр

        with self.assertRaises(ValueError):
            get_mask_card_number("12345678901234567")  # 17 цифр

    def test_get_mask_card_number_non_numeric(self):
        """Тест обработки нечислового номера карты."""
        with self.assertRaises(ValueError):
            get_mask_card_number("abcdefghijklmnop")

        with self.assertRaises(ValueError):
            get_mask_card_number("7000a922b960c361")

    def test_get_mask_account_valid(self):
        """Тест корректной маскировки номера счёта."""
        # Тестовые данные: (входной номер, ожидаемый результат)
        test_cases = [
            ("73654108430135874305", "**4305"),
            ("1234567890", "**90"),
            ("00000000000000000001", "**0001"),
            ("99999999999999999999", "**9999"),
        ]

        for account_number, expected in test_cases:
            with self.subTest(account_number=account_number):
                result = get_mask_account(account_number)
                self.assertEqual(result, expected)

    def test_get_mask_account_with_spaces(self):
        """Тест маскировки номера счёта с пробелами."""
        input_account = "7365 4108 4301 3587 4305"
        expected = "**4305"
        result = get_mask_account(input_account)
        self.assertEqual(result, expected)

    def test_get_mask_account_non_numeric(self):
        """Тест обработки нечислового номера счёта."""
        with self.assertRaises(ValueError):
            get_mask_account("abcdefghij")

        with self.assertRaises(ValueError):
            get_mask_account("7365a108b430c358d430e")

    def test_get_mask_account_empty(self):
        """Тест обработки пустого номера счёта."""
        with self.assertRaises(ValueError):
            get_mask_account("")

    def test_get_mask_account_short(self):
        """Тест обработки короткого номера счёта (менее 4 цифр)."""
        test_cases = ["1", "12", "123"]
        expected_results = ["**1", "**12", "**123"]

        for account, expected in zip(test_cases, expected_results):
            with self.subTest(account=account):
                result = get_mask_account(account)
                self.assertEqual(result, expected)



if __name__ == "__main__":
    unittest.main()
