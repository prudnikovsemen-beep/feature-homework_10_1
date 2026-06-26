from datetime import datetime
from typing import Union

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(line: str) -> str:
    """
    Обрабатывает строку, содержащую тип и номер (карты или счёта),
    и возвращает строку с замаскированным номером.

    Примеры:
        "Visa Platinum 7000792289606361" -> "Visa Platinum 7000 79** **** 6361"
        "Счет 73654108430135874305"      -> "Счет **4305"

    Логика:
        - Ищем в конце строки последовательность цифр.
        - Если длина 16 — считаем картой.
        - Иначе, если есть слово "Счет" (регистронезависимо) или длина не 16 — считаем счётом.

    :param line: Строка вида "<тип> <номер>"
    :return: Строка с замаскированным номером
    """
    # Находим последний непрерывный блок цифр в строке
    digits_end = len(line)
    while digits_end > 0 and line[digits_end - 1].isdigit():
        digits_end -= 1

    number_part = line[digits_end:].strip()
    prefix_part = line[:digits_end].strip()

    if not number_part.isdigit():
        raise ValueError("No valid numeric account/card number found in the input string.")

    # Определяем тип по длине и/или по префиксу
    if len(number_part) == 16:
        masked_number = get_mask_card_number(number_part)
    else:
        # Для счёта: даже если длина не 16, считаем счётом
        masked_number = get_mask_account(number_part)

    return f"{prefix_part} {masked_number}"


def get_date(iso_string: str) -> str:
    """
    Преобразует строку даты в формате ISO 8601 в формат ДД.ММ.ГГГГ.

    Пример:
        "2024-03-11T02:26:18.671407" -> "11.03.2024"

    :param iso_string: Строка даты в формате ISO
    :return: Дата в формате ДД.ММ.ГГГГ
    """
    dt = datetime.fromisoformat(iso_string)
    return dt.strftime("%d.%m.%Y")
