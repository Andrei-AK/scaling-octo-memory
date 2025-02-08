from typing import Any

card_number = 1234560000001234
account_number = "11111111111111115567"


def get_mask_card_number(user_card_number: Any) -> str:
    """Маскировка номера карты прользователя"""
    user_card_number = str(user_card_number)
    split_masked_card_number: str = ""
    if user_card_number.isdigit() and len(user_card_number) == 16:
        masked_card_number = user_card_number[:6] + "*" * (len(user_card_number) - 10) + user_card_number[12:16]
        for i in range(0, len(masked_card_number), 4):
            split_masked_card_number += masked_card_number[i : i + 4] + " "
            #split_masked_card_number = split_masked_card_number.strip()
        return split_masked_card_number
    return "Номер карты введен неверно!"


def get_mask_account(user_account_number: Any) -> str:
    """Маскировка номера аккаунта прользователя"""
    user_account_number = str(user_account_number)
    if user_account_number.isdigit() and len(user_account_number) == 20:
        masked_account_number: str = "**" + user_account_number[-4:]
        return masked_account_number
    return "Номер аккаунта введен неверно!"


print(get_mask_card_number(card_number))
print(get_mask_account(account_number))
