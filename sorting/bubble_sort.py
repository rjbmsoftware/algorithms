import unittest


def bubble_sort(values: list) -> None:
    """
    sorts ascending

    in place sort

    complexity
        time: n squared
        space: n 

    implementation of the bubble sort algorithm
    that will work on any type that can be
    compared with <>== that
    """
    for i in range(1, len(values)):
        for j in range(len(values) - i):
            next = j + 1
            if values[j] > values[next]:
                values[j], values[next] = values[next], values[j]

    return values


class BubbleSortTest(unittest.TestCase):

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
        bubble_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_empty_is_sorted(self):
        input = []
        bubble_sort(input)
        self.assertTrue(self.is_sorted(input))
        
    def test_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bubble_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_same(self):
        input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        bubble_sort(input)
        self.assertTrue(self.is_sorted(input))


if __name__ == "__main__":
    unittest.main()
