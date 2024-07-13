import unittest

def merge_sort(input) -> list:
    """
    top down merge sort implementation

    complexity
        time 
            n log n
            divide and conquer, then recombination
        space n

    1. repeatedly split the array into single value lists
    2. merge split lists by comparing the leading values
    
    after all the lists are merged the list is sorted
    """
    if len(input) <= 1:
        return input
    
    left_half_of_input = input[:len(input) // 2]
    right_half_of_input = input[len(input) // 2:]
    return merge_lists(
        merge_sort(left_half_of_input),
        merge_sort(right_half_of_input)
    )
 

def merge_lists(left_list: list, right_list: list) -> list:
    """
    returns a sorted list containing all the elements
    from the already sorted arguments
    """
    merged_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left_list) or right_index < len(right_list):
        if left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                merged_list.append(left_list[left_index])
                left_index += 1
            else:
                merged_list.append(right_list[right_index])
                right_index += 1
        elif left_index < len(left_list):
            merged_list.append(left_list[left_index])
            left_index += 1
        else:
            merged_list.append(right_list[right_index])
            right_index += 1
    
    return merged_list

class MergeSortTest(unittest.TestCase):

    def test_merge_doubles_in_order(self):
        output = merge_lists([1, 2], [3, 4])
        self.assertEqual(output, [1, 2, 3, 4])

    def test_merge_doubles_out_of_order(self):
        output = merge_lists([3, 4], [1, 2])
        self.assertEqual(output, [1, 2, 3, 4])

    def test_merge_single(self):
        output = merge_lists([1], [2])
        self.assertEqual(output, [1, 2])

    def test_left_empty(self):
        output = merge_lists([], [1])
        self.assertEqual(output, [1])

    def test_right_empty(self):
        output = merge_lists([1], [])
        self.assertEqual(output, [1])


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
            

    def test_max_to_min(self):
        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        output = merge_sort(input)
        self.assertTrue(self.is_sorted(output))

    def test_empty_is_sorted(self):
        input = []
        output = merge_sort(input)
        self.assertTrue(self.is_sorted(output))
        
    def test_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        output = merge_sort(input)
        self.assertTrue(self.is_sorted(output))

    def test_same(self):
        input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        output = merge_sort(input)
        self.assertTrue(self.is_sorted(output))


if __name__ == '__main__':
    unittest.main()