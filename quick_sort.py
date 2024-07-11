import unittest


def quick_sort(input: list, start_index: int, end_index: int) -> None:
    """
    inplace quick sort implementation
    indexes are inclusive

    complexity
        time n log n
        space log n

    1. call partition on list
    2. output from partition is our partition point
    3. call quick sort on both halves

    lists that has a length less than or equal to one are sorted
    """
    if start_index >= end_index:
        return
    
    partition_point = partition(input, start_index, end_index)

    quick_sort(input, start_index, partition_point - 1)
    quick_sort(input, partition_point + 1, end_index)


def partition(input: list, start_index: int, end_index: int) -> int:
    """
    sort the array into two halves, less than or equal to 
    the pivot value and greater than the pivot value
    returning the pivot index, in place.

    high value is the end of the array
    swap the pivot value into the split point between the
    low high halves.
    """
    i = start_index -1
    pivot_value = input[end_index]

    for j in range(start_index, end_index):
        if input[j] <= pivot_value:
            i += 1
            input[i], input[j] = input[j], input[i]
            
    input[i + 1], input[end_index] = input[end_index], input[i + 1]
    return i + 1


class QuickSortTest(unittest.TestCase):

    def test_partition_is_the_end_value_moved_to_the_centre(self):
        input = [8, 7, 3, 2, 4]
        partition(input, 0, len(input) -1)
        self.assertEqual(input[2], 4)


    def is_sorted(self, input: list) -> bool:
        """
        returns if the list is sorted
        """
        if len(input) <= 1:
            return True
        
        i = 0
        max_index = len(input) -1
        while i < max_index:
            if input[i] > input[i + 1]:
                return False
            
            i += 1

        return True

    def test_even_length(self): 
        input = [4, 3, 2, 1]
        quick_sort(input, 0, len(input) - 1)
        self.assertTrue(self.is_sorted(input))

    def test_odd_length(self):
        input = [5, 4, 3, 2, 1]
        quick_sort(input, 0, len(input) - 1)
        self.assertTrue(self.is_sorted(input))

    def test_single_value_list(self):
        input = [0]
        quick_sort(input, 0, len(input) - 1)
        self.assertTrue(self.is_sorted(input))

    def test_empty_is_sorted(self):
        input = []
        quick_sort(input, 0, 0)
        self.assertTrue(self.is_sorted(input))

    def test_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        quick_sort(input, 0, len(input) - 1)
        self.assertTrue(self.is_sorted(input))

if __name__ == '__main__':
    unittest.main()