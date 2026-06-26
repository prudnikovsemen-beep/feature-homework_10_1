import pytest
from src.masks import get_mask_card_number, get_mask_account


class TestGetMaskCardNumber:
    def test_valid_card_number(self):
        card = "7000792289606361"
        expected = "7000 79** **** 6361"
        assert get_mask_card_number(card) == expected

    def test_invalid_length(self):
        with pytest.raises(ValueError):
            get_mask_card_number("123456789012345")  # 15 digits

    def test_non_digit_input(self):
        with pytest.raises(ValueError):
            get_mask_card_number("700079228960636A")


class TestGetMaskAccount:
    def test_valid_account_number(self):
        account = "73654108430135874305"
        expected = "**4305"
        assert get_mask_account(account) == expected

    def test_short_account_number(self):
        with pytest.raises(ValueError):
            get_mask_account("123")

    def test_non_digit_account(self):
        with pytest.raises(ValueError):
            get_mask_account("1234ABCD")
