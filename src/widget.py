import string

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_information: str) -> str:
    """Проверка корректности полученных данных"""
    cnt: int = 0
    user_information = str(user_information)
    if user_information is not None:
        for i in user_information:
            if i.isdigit() or i in string.punctuation:
                cnt += 1
        if cnt == 16:
            return get_mask_card_number(user_information)
        if cnt == 20:
            return get_mask_account(user_information)
        else:
            return "Данные введены неверно!"


def get_date(date_valid: str) -> str:
    date_valid = date_valid[8:10] + "." + date_valid[5:7] + "." + date_valid[:4]
    return date_valid
