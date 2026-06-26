def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.

    Формат вывода: XXXX XX** **** XXXX
    - видны первые 6 цифр и последние 4 цифры
    - остальные символы заменяются на '*'
    - номер разбит на блоки по 4 цифры, разделённые пробелами

    :param card_number: Номер карты в виде строки
    :return: Замаскированный номер карты
    """
    if not card_number.isdigit() or len(card_number) != 16:
        raise ValueError("Card number must be a 16-digit string.")

    first_six = card_number[:6]
    last_four = card_number[-4:]

    # Формируем маску: первые 6, затем 6 звёздочек, затем последние 4
    masked_middle = "*" * 6

    # Собираем блоки по 4 символа
    block1 = first_six[:4]
    block2 = first_six[4:] + masked_middle[:2]
    block3 = masked_middle[2:] + last_four[:2]
    block4 = last_four[2:]

    return f"{block1} {block2} {block3} {block4}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счёта.

    Формат вывода: **XXXX
    - видны только последние 4 цифры
    - перед ними две звёздочки

    :param account_number: Номер счёта в виде строки
    :return: Замаскированный номер счёта
    """
    if not account_number.isdigit():
        raise ValueError("Account number must contain only digits.")

    if len(account_number) < 4:
        raise ValueError("Account number must have at least 4 digits.")

    last_four = account_number[-4:]
    return f"**{last_four}"
