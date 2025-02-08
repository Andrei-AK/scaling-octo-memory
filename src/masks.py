def get_mask_card_number(user_card_number: str):
    """Маскировка номера карты прользователя"""
    split_masked_card_number = ''
    cnt = 0
    for i in user_card_number:
        if not i.isdigit():
            split_masked_card_number += i
        else:
            if cnt % 4 == 0 and cnt != 0:
                split_masked_card_number += " "
            if 6 <= cnt <= 11:
                split_masked_card_number += "*"
            else:
                split_masked_card_number += i
            cnt += 1
    return split_masked_card_number


def get_mask_account(user_account_number: str):
    """Маскировка номера аккаунта прользователя"""
    masked_account_number: str = ''
    cnt: int = 0
    for i in user_account_number:
        if not i.isdigit() or cnt > 20:
            masked_account_number += i
        elif cnt == 20:
            masked_account_number += '**'
        cnt += 1
    return masked_account_number
