import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card,expected",
    [
        ("4276123456789012", "4276********9012"),
        (" 4276 1234 5678 9012 ", "4276********9012"),
        ("1234", None),
        ("", None),
        (None, None),
    ],
)
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize(
    "account,expected",
    [
        ("40817810000001234567", "40817**********4567"),
        ("40702810500000000001", "40702**********0001"),
        ("123", None),
        ("", None),
        (None, None),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
