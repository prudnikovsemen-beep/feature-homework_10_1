from typing import List, Dict, Any, Optional


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по полю state.

    :param operations: список словарей с данными об операциях
    :param state: значение поля state для фильтрации (по умолчанию 'EXECUTED')
    :return: новый список словарей, где state == state
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате (поле date).

    Формат даты: ISO 8601 (например, '2019-07-03T18:35:29.512364').
    Такие строки можно сортировать лексикографически.

    :param operations: список словарей с данными об операциях
    :param reverse: если True — сортировка по убыванию (сначала новые), иначе по возрастанию
    :return: новый отсортированный список
    """
    # Создаём новый список, не меняя исходный
    return sorted(operations, key=lambda op: op.get("date", ""), reverse=reverse)
