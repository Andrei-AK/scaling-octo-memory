import logging
from typing import Any

logging.basicConfig(encoding="UTF-8")
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler('../logs/masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(user_card_number: str) -> str | None | Any:
    """Маскировка номера карты прользователя"""
    logger.debug(f"Функция начала работу {get_mask_card_number.__name__}")
    try:
        split_masked_card_number: str = ""
        cnt: int = 0
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
        logger.debug(f"Функция {get_mask_card_number.__name__} завершила свою работу")
        return split_masked_card_number
    except ValueError:
        logger.error(f"Возникла ошибка {ValueError} при выполнении функции {get_mask_card_number.__name__}")



def get_mask_account(user_account_number: str) -> str:
    """Маскировка номера аккаунта прользователя"""
    logger.debug(f"Функция {get_mask_account.__name__} начала работу")
    try:
        masked_account_number: str = ""
        cnt: int = 0
        for i in user_account_number:
            if not i.isdigit() or cnt > 20:
                masked_account_number += i
            elif cnt == 20:
                masked_account_number += "**"
            cnt += 1
        logger.debug(f"Функция {get_mask_account.__name__} завершила работу")
        return masked_account_number
    except ValueError:
        logger.error(f"Возникла ошибка {ValueError} при выполнении функции {get_mask_account.__name__}")
