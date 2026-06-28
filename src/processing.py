from datetime import datetime


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations (list[dict]): Список словарей с операциями.
        state (str): Статус для фильтрации (по умолчанию 'EXECUTED').

    Returns:
        list[dict]: Отфильтрованный список операций.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате.

    Args:
        operations (list[dict]): Список словарей с операциями.
        reverse (bool): Порядок сортировки (True — убывание, False — возрастание).

    Returns:
        list[dict]: Отсортированный список операций.
    """

    def parse_date(date_str: str) -> datetime:
        return datetime.fromisoformat(date_str.replace("Z", "+00:00"))

    return sorted(operations, key=lambda op: parse_date(op["date"]), reverse=reverse)
