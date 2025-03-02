from typing import Iterator


def recursive_search(some_dict: dict, target: str) -> bool:
    if isinstance(some_dict, dict):
        if some_dict.get("code") == target:
            return True
        for v in some_dict.values():
            if recursive_search(v, target):
                return True
    elif isinstance(some_dict, list):
        for item in some_dict:
            if recursive_search(item, target):
                return True
    return False


def filter_by_currency(data: list, target: str) -> Iterator[list | None]:
    filtered_transactions = [transaction for transaction in data if recursive_search(transaction, target) is True]
    yield filtered_transactions


def transaction_descriptions(data: list) -> Iterator[str]:
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
    while True:
        yield initial_value
        if initial_value < final_value:
            initial_value += 1
        else:
            break
