from typing import Any


def filter_by_state(
    operations: list[dict[str, Any]],
    state: str = "EXECUTED",
) -> list[dict[str, Any]]:
    """
    Фильтрует список операций по полю state.

    :param operations: список словарей с данными об операциях
    :param state: значение поля state для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, где state == state
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: list[dict[str, Any]],
    reverse: bool = True,
) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате (поле date).

    Формат даты: ISO 8601 (например, '2019-07-03T18:35:29.512364').
    Такие строки можно сортировать лексикографически.

    :param operations: список словарей с данными об операциях
    :param reverse: если True — сортировка по убыванию (сначала новые), иначе по возрастанию
    :return: новый отсортированный список
    """
    return sorted(
        operations,
        key=lambda op: op.get("date", ""),
        reverse=reverse,
    )
