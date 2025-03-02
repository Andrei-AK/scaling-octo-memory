import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    recursive_search,
    transaction_descriptions,
)


@pytest.mark.parametrize("initial_num, final_num, expected_result", [(1, 5, [1, 2, 3, 4, 5]), (5, 7, [5, 6, 7])])
def test_card_number_generator(initial_num: int, final_num: int, expected_result: int) -> None:
    assert list(card_number_generator(initial_num, final_num)) == expected_result


def test_recursive_search(dict_of_date: dict) -> None:
    assert recursive_search(dict_of_date, "USD") is True
    assert recursive_search({}, "") is False
    assert recursive_search(dict_of_date, "") is False


def test_filter_by_currency(date_for_generators: list) -> None:
    expect_result = [
        {
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 11776614605963066702",
        },
        {
            "date": "2019-04-04T23:20:05.206878",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Счет 75651667383060284188",
        },
        {
            "date": "2018-08-19T04:27:37.904916",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "id": 895315941,
            "operationAmount": {"amount": "56883.54", "currency": {"code": "USD", "name": "USD"}},
            "state": "EXECUTED",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    generator = filter_by_currency(date_for_generators, "USD")
    assert expect_result == next(generator)
    expect_result = []
    generator = filter_by_currency([], "")
    assert expect_result == next(generator)


def test_transaction_descriptions(date_for_generators: list) -> None:
    generator = transaction_descriptions(date_for_generators)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
