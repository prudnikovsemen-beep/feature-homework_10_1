# src/widget.py
from datetime import datetime, timedelta
from typing import Optional

from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(line: str) -> Optional[str]:
    if not line or not isinstance(line, str):
        return None

    digits_end = len(line)
    while digits_end > 0 and line[digits_end - 1].isdigit():
        digits_end -= 1

    number_part = line[digits_end:].strip()
    prefix_part = line[:digits_end].strip()

    if not number_part.isdigit() or len(number_part) == 0:
        return None

    if len(number_part) == 16:
        masked_number = get_mask_card_number(number_part)
        if masked_number is None:
            return None
    else:
        masked_number = get_mask_account(number_part)
        if masked_number is None:
            return None

    if prefix_part == "":
        return masked_number

    return f"{prefix_part} {masked_number}"


def get_date(iso_string: str) -> Optional[str]:
    if not iso_string or not isinstance(iso_string, str):
        return None

    iso_string = iso_string.strip()
    if iso_string == "":
        return None

    try:
        dt = datetime.fromisoformat(iso_string)

        # Хитрость для округления секунд: добавляем полсекунды, потом убираем микросекунды
        dt_rounded = dt + timedelta(microseconds=500000)
        dt_rounded = dt_rounded.replace(microsecond=0)

        return dt_rounded.strftime("%d.%m.%Y %H:%M:%S")
    except (ValueError, TypeError):
        return None
