def filter_by_state(list_for_sort: list, sort_key: str = "EXECUTED") -> list:
    """Фильтруем словари из списка по значению sotr_key в ключе state"""
    sorted_list = []
    for i in list_for_sort:
        if i["state"] == sort_key:
            sorted_list.append(i)
    return sorted_list


def sort_by_date(list_for_sort: list, sort_direction: bool = True) -> list:
    """Сортируем список по дате"""
    sorted_list = sorted(list_for_sort, key=lambda element: element["date"], reverse=sort_direction)
    return sorted_list
