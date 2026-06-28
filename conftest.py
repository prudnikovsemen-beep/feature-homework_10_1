import pytest

@pytest.fixture
def card_numbers():
    return [
        "4276123456789012",
        " 4276 1234 5678 9012 ",
        "4276-1234-5678-9012",
        "1234",          # слишком короткий
        "",              # пустой
        None,            # None
    ]

@pytest.fixture
def account_numbers():
    return [
        "40817810000001234567",
        "40702810500000000001",
        "123",           # слишком короткий
        "",
        None,
    ]

@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-01T08:17:53.596580"},
        {"id": 2, "state": "CANCELED", "date": "2019-07-02T06:34:43.162004"},
        {"id": 3, "state": "EXECUTED", "date": "2019-07-03T07:07:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2019-07-04T12:00:00.123456"},
    ]
