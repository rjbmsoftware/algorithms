from typing import Optional
import unittest

def binary_search(input: list, target_value) -> Optional[int]:
    """
    input must be sorted in ascending order
    
    return value is optional as it is not guaranteed the 
    value is in the input list, return value is the index
    of the target value
    
    Complexity
        time O(log n)
        space O(1)
    """

    low = 0
    high = len(input) - 1
    mid: int

    while low < high:
        mid = (high - low) // 2 + low
        if input[mid] == target_value:
            return mid
        elif input[mid] < target_value:
            high = mid - 1
        else:
            low = mid + 1

    return None

class BinarySearchTest(unittest.TestCase):

    def test_input_no_values(self):
        input = []
        target = 99
        actual_index = binary_search(input, target)
        self.assertIsNone(actual_index)

    def test_input_does_not_contain_value(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 99
        actual_index = binary_search(input, target)
        self.assertIsNone(actual_index)

    def test_odd_length_contains_value(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        expected_index = 4
        actual_index = binary_search(input, target)
        self.assertIsNotNone(actual_index)
        self.assertEqual(expected_index, actual_index)

    def test_even_length_contains_value(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 5
        expected_index = 4
        actual_index = binary_search(input, target)
        self.assertIsNotNone(actual_index)
        self.assertEqual(expected_index, actual_index)

if __name__ == '__main__':
    unittest.main()