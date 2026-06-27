import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED", "PENDING"])
def test_filter_by_state(transactions, state):
    filtered = filter_by_state(transactions, state)
    for t in filtered:
        assert t["state"] == state


def test_filter_by_state_no_matches(transactions):
    result = filter_by_state(transactions, "UNKNOWN_STATE")
    assert result == []


@pytest.mark.parametrize("reverse", [True, False])
def test_sort_by_date(transactions, reverse):
    sorted_list = sort_by_date(transactions, reverse=reverse)
    # Проверка, что список отсортирован
    dates = [t["date"] for t in sorted_list]
    if reverse:
        assert dates == sorted(dates, reverse=True)
    else:
        assert dates == sorted(dates)


def test_sort_by_date_same_dates():
    data = [
        {"date": "2020-01-01T10:00:00"},
        {"date": "2020-01-01T10:00:00"},
        {"date": "2020-01-01T10:00:00"},
    ]
    result = sort_by_date(data, reverse=False)
    assert len(result) == 3
