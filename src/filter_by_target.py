import re
from collections import Counter


def filter_by_state(transactions, target):
        filtered_transactions = []
        transactions = filter(None, transactions)
        pattern = re.compile(re.escape(target), re.I)
        for transaction in transactions:
            if transactions and "state" in transaction and pattern.search(str(transaction["state"])):
                filtered_transactions.append(transaction)
        return filtered_transactions


def filter_by_description(transactions, target):
        filtered_transactions = []
        transactions = filter(None, transactions)
        pattern = re.compile(re.escape(target), re.I)
        for transaction in transactions:
            if transactions and "description" in transaction and pattern.search(str(transaction["description"])):
                filtered_transactions.append(transaction)
        return filtered_transactions



def count_transaction(transactions, categories):
    counted_categories = Counter()
    for category in categories:
        pattern = re.compile(re.escape(category), re.I)
        for transaction in transactions:
            if "description" in transaction and pattern.search(str(transaction["description"])):
                counted_categories[category] += 1
    return dict(counted_categories)
