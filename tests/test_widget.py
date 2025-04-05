import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "date_valid, returned_date",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2022-01-12T02:26:18.671407", "12.01.2022")],
)
def test_date_valid(date_valid: str, returned_date: str) -> None:
    assert get_date(date_valid) == returned_date


@pytest.mark.parametrize(
    "user_data, returned_date",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 06831982476737658", "Данные введены неверно!"),
        ("", "Данные введены неверно!"),
    ],
)
def test_mask_account_card(user_data: str, returned_date: str) -> None:
    assert mask_account_card(user_data) == returned_date
