import string
from src.masks import get_mask_account, get_mask_card_number

# user_information = "Visa Platinum 7000792289606361"
user_information = "Счет 73654108430135874305"


def check_correct_data(user_information: str) -> int:
    """Проверка корректности полученных данных"""
    cnt: int = 0
    for i in user_information:
        if i.isdigit() or i in string.punctuation:
            cnt += 1
    if cnt == 16:  # 1-card number, 2-account number, 0-fail input
        return 1
    if cnt == 20:
        return 2
    else:
        return 0


def mask_account_card(user_card_info: str) -> str:
    """Маскирует номер счета/карты прользователя"""
    check_result: int = check_correct_data(user_card_info)
    if not check_result == 0:
        if check_result == 1:
            masked_user_info: str = get_mask_card_number(user_card_info)
            return masked_user_info
        if check_result == 2:
            masked_user_info = get_mask_account(user_card_info)
            return masked_user_info
    return "Даные введены неверно!"


def get_date(date_valid: str) -> str:
    date_valid = date_valid[8:10] + "." + date_valid[5:7] + "." + date_valid[:4]
    return date_valid


print(get_date(date_valid="2024-03-11T02:26:18.671407"))
print(mask_account_card(user_information))
