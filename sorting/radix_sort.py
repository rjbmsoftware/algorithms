import unittest

from sort_utils import is_sorted


def radix_sort(values: list[int]) -> list[int]:
    """
    Radix sort implementation of base 10 integers by applying counting sort from the right most
    digit then using counting sort again on the digit to the left of the right most.

    Stable sort not in place

    complexity
        time:

        space:
    """
    passes = len(str(max(values)))
    output_list = values[:]
    for i in range(passes, 0, -1):
        output_list = counting_sort(output_list, i)

    return output_list


def counting_sort(values: list[int], power: int) -> list[int]:
    """
    Counting sort of base 10 integers

    power the power of 10 to select which values are used to sort the list, 1 for units, 2 for
    10s...
    """
    # map values to a digit
    value_to_digit_value = {}
    for value in values:
        digit = value
        if digit >= 10 ** (power - 1):
            for _ in range(power - 1):
                digit //= 10

            digit %= 10
        else:
            digit = 0
        value_to_digit_value[value] = digit

    range_list = [0] * (max(value_to_digit_value.values()) + 1)

    # count the frequency of each value into range list
    for value in values:
        range_list[value_to_digit_value[value]] += 1

    # calculate the starting index of the next value by adding the value to the left
    for i in range(len(range_list) - 1):
        range_list[i + 1] += range_list[i]

    # shift range_list values along one by one so the next value knows which index to start
    for i in range(len(range_list) - 1, 0, -1):
        range_list[i] = range_list[i - 1]

    range_list[0] = 0
    output_list = [0] * len(values)

    for value in values:
        index = range_list[value_to_digit_value[value]]
        output_list[index] = value
        range_list[value_to_digit_value[value]] += 1

    return output_list


class RadixSortTest(unittest.TestCase):

    def test_reverse(self):
        values = [1234, 123, 12, 1]
        output_values = radix_sort(values)
        self.assertEqual(output_values, [1, 12, 123, 1234])


class CountingSortTest(unittest.TestCase):

    def test_same_tens_different_units_sorted_by_tens_same(self):
        values = [99, 98, 97, 96, 95, 94, 93, 92, 91]
        output_values = counting_sort(values, 2)
        self.assertEqual(values, output_values)

    def test_units_sorted(self):
        values = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        output_values = counting_sort(values, 1)
        self.assertEqual(output_values, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_descending_tens_ascending_units(self):
        values = [91, 82, 73, 64, 55, 46, 37, 28, 19]
        output_values = counting_sort(values, 2)
        self.assertEqual(len(values), len(output_values))
        self.assertTrue(is_sorted(output_values))

    def test_integers_max_to_min_power_of_ten_less(self):
        values = [40, 4, 30, 3, 20, 2, 10, 1]
        output_values = counting_sort(values, 2)
        self.assertEqual(output_values, [4, 3, 2, 1, 10, 20, 30, 40])

    def test_handle_zero_values(self):
        values = [1000, 100, 10, 0, 0, 0]
        output_values = counting_sort(values, 1)
        self.assertEqual(values, output_values)


if __name__ == '__main__':
    unittest.main()
