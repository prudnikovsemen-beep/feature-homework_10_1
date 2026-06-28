from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счёта в строке.

    Args:
        input_string (str): Строка, содержащая тип и номер карты/счёта.
            Примеры: "Visa Platinum 7000792289606361", "Счет 73654108430135874305".

    Returns:
        str: Строка с замаскированным номером.
    """
    # Разделяем строку на части, последняя часть — номер
    parts = input_string.split()
    if not parts:
        return input_string

    number = parts[-1]  # последний элемент — номер
    prefix = " ".join(parts[:-1])  # всё, кроме номера

    # Проверяем, является ли номер счётом (начинается со слова "Счёт" или "Счет")
    if prefix.endswith("Счет") or prefix.endswith("Счёт"):
        masked_number = get_mask_account(number)
    else:
        # Предполагаем, что это карта
        masked_number = get_mask_card_number(number)

    return f"{prefix} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407".

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime

    # Парсим дату из строки ISO
    dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
    # Форматируем в нужный формат
    return dt.strftime("%d.%m.%Y")
