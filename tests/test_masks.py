import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ],
)
def test_get_mask_card_number(card_number: str, mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account_number, mask_account_number",
    [("Счет 64686473678894779589", "Счет **9589"), ("Счет 73654108430135874305", "Счет **4305")],
)
def test_get_mask_account(account_number: str, mask_account_number: str) -> None:
    assert get_mask_account(account_number) == mask_account_number
