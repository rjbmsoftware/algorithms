from typing import TypeVar
import unittest

T = TypeVar('T')


def exponential_search(values: list[T], value: T) -> int | None:
    """
    Searches the values for value returning the index in the list of the found value otherwise None,
    values must be sorted

    This search is useful over binary search where the values are more likely to be at the beginning
    of the list

    1. find the range the value may reside in
    2. use binary search on the range of values

    complexity
        time:

        space:

    """
    start_index = 0
    end_index = 1

    while start_index <= end_index:

        value_found = values[start_index] == value
        if value_found:
            return start_index
        
        if values[end_index] < value:
            start_index = end_index
            end_index *= 2


    return None



class ExponentialSearchTest(unittest.TestCase):
    
    def test_contains_value(self):
        values = [1, 2, 3, 4, 5]
        value = 3
        found_index = exponential_search(values, value)
        self.assertIsNotNone(found_index)
        self.assertEqual(found_index, 2)


if __name__ == '__main__':
    unittest.main()
