import pytest
from src.widget import mask_account_card, get_date


class TestMaskAccountCard:
    def test_card_visa_platinum(self):
        line = "Visa Platinum 7000792289606361"
        expected = "Visa Platinum 7000 79** **** 6361"
        assert mask_account_card(line) == expected

    def test_card_maestro(self):
        line = "Maestro 1596837868705199"
        expected = "Maestro 1596 83** **** 5199"
        assert mask_account_card(line) == expected

    def test_account_long_number(self):
        line = "Счет 73654108430135874305"
        expected = "Счет **4305"
        assert mask_account_card(line) == expected

    def test_multiple_examples(self):
        examples = [
            ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
            ("Счет 64686473678894779589", "Счет **9589"),
            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
            ("Счет 35383033474447895560", "Счет **5560"),
            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
            ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
            ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
            ("Счет 73654108430135874305", "Счет **4305"),
        ]
        for inp, expected in examples:
            assert mask_account_card(inp) == expected

    def test_invalid_no_digits(self):
        with pytest.raises(ValueError):
            mask_account_card("Visa Platinum ABCD")


class TestGetDate:
    def test_basic_conversion(self):
        iso_str = "2024-03-11T02:26:18.671407"
        expected = "11.03.2024"
        assert get_date(iso_str) == expected

    def test_different_date(self):
        iso_str = "2023-12-31T23:59:59.123456"
        expected = "31.12.2023"
        assert get_date(iso_str) == expected
