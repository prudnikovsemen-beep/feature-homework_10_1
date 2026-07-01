# src/masks.py

def get_mask_card_number(card_number):
    if card_number is None:
        return None

    clean_number = str(card_number).replace(" ", "").strip()

    if not clean_number.isdigit() or len(clean_number) != 16:
        return None

    return f"{clean_number[:4]}********{clean_number[-4:]}"


def get_mask_account(account_number):
    if account_number is None:
        return None

    clean_number = str(account_number).replace(" ", "").strip()

    if not clean_number.isdigit():
        return None

    if len(clean_number) < 9:
        return None

    # Важно: ровно 10 звёздочек, как хочет тест
    return f"{clean_number[:5]}**********{clean_number[-4:]}"
