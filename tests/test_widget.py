import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "value,expected_type",
    [
        ("4276123456789012", "card"),
        ("40817810000001234567", "account"),
        ("not a number", None),
    ],
)
def test_mask_account_card_type_detection(value, expected_type):
    # Здесь зависит от вашей реализации: либо возвращает тип, либо сразу маску.
    # Если сразу маска — проверяйте формат маски.
    result = mask_account_card(value)
    if expected_type == "card":
        assert result.startswith("4") and "****" in result
    elif expected_type == "account":
        assert "****" in result and not result.startswith("42")
    else:
        assert result is None


@pytest.mark.parametrize(
    "date_str,expected_date_str",
    [
        ("2019-07-01T08:17:53.596580", "01.07.2019 08:17:54"),
        ("2019-07-02T06:34:43.162004", "02.07.2019 06:34:43"),
        ("", None),
        ("invalid", None),
    ],
)
def test_get_date(date_str, expected_date_str):
    assert get_date(date_str) == expected_date_str
