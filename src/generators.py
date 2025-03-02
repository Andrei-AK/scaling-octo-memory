from typing import Generator, Iterator


def filter_by_currency(data: list, target: str) -> Generator[dict, None, None]:
    """Фильтрация списка транзакций по валюте"""
    for transaction in data:
        if transaction["operationAmount"]["currency"]["code"] == target:
            yield transaction


print(list(filter_by_currency([], "")))


def transaction_descriptions(data: list) -> Iterator[str]:
    """Вывод описания операций"""
    cnt = 0
    transaction_description = list(
        (
            transaction.get("description")
            for transaction in data
            if any(key == "description" for key, val in transaction.items()) is True
        )
    )
    while True:
        yield transaction_description[cnt]
        if cnt in range(len(transaction_description) - 1):
            cnt += 1
        else:
            break


def card_number_generator(initial_value: int, final_value: int) -> Iterator[int]:
    """Генерирование номера карты между начальным и конечным значением"""
    while True:
        yield initial_value
        if initial_value < final_value:
            initial_value += 1
        else:
            break
