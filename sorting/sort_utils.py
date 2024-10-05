def is_sorted(values: list) -> bool:
    """
    returns if the list is sorted
    """
    if len(values) <= 1:
        return True

    i = 0
    max_index = len(values) - 1
    while i < max_index:
        if values[i] > values[i + 1]:
            return False

        i += 1

    return True
