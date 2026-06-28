def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты в формате XXXX XX** **** XXXX.

    Args:
        card_number (str): Номер карты (16 цифр).

    Returns:
        str: Замаскированный номер карты.
    """
    # Удаляем пробелы, если они есть
    cleaned_number = card_number.replace(' ', '')

    # Проверяем длину номера карты
    if len(cleaned_number) != 16 or not cleaned_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формируем маску: первые 6 цифр, затем 6 звёздочек, затем последние 4 цифры
    masked = (
        f"{cleaned_number[:4]} {cleaned_number[4:6]}**"
        f" **** {cleaned_number[-4:]}"
    )
    return masked



def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта в формате **XXXX.

    Args:
        account_number (str): Номер счёта.

    Returns:
        str: Замаскированный номер счёта.
    """
    # Удаляем пробелы, если они есть
    cleaned_number = account_number.replace(' ', '')

    # Проверяем, что номер состоит только из цифр
    if not cleaned_number.isdigit():
        raise ValueError("Номер счёта должен содержать только цифры")

    # Берём последние 4 цифры и добавляем две звёздочки перед ними
    return f"**{cleaned_number[-4:]}"