import unittest


def insertion_sort(values: list) -> None:
    # TODO move the is_sorted method out into a helper
    pass


class InsertionSortTest(unittest.TestCase):

    def is_sorted(self, input: list) -> bool:
        """
        returns if the list is sorted
        """
        if len(input) <= 1:
            return True

        i = 0
        max_index = len(input) - 1
        while i < max_index:
            if input[i] > input[i + 1]:
                return False

            i += 1

        return True

    def test_max_to_min(self):
        input = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_empty_is_sorted(self):
        input = []
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))
        
    def test_already_sorted(self):
        input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))

    def test_same(self):
        input = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        insertion_sort(input)
        self.assertTrue(self.is_sorted(input))



if __name__ == "__main__":
    unittest.main()
