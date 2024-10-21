import unittest


def radix_sort(values: list[int]) -> list[int]:
    """
    Radix sort implementation of base 10 integers by applying counting sort from the right most
    digit then using counting sort again on the digit to the left of the right most.

    Stable sort not in place

    complexity
        time:

        space:
    """


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
        for _ in range(power):
            digit %= 10
        value_to_digit_value[value] = digit

    range_list = [0] * max(value_to_digit_value.values())

    for value in values:
        range_list[value_to_digit_value[value]] += 1

    # shift range_list values along one by one so the next value knows which index to start
    for i in range(len(range_list) - 2, 0, -1):
        range_list[i] = range_list[-1]

    range_list[0] = 0
    output_list = [0] * len(values)

    for value in values:
        index = range_list[value_to_digit_value[value]]
        output_list[index] = value

    return output_list


class RadixSortTest(unittest.TestCase):
    pass


class CountingSortTest(unittest.TestCase):

    def test_same_tens_different_units_sorted_by_tens_same(self):
        values = [99, 98, 97, 96, 95, 94, 93, 92, 91]
        output_values = counting_sort(values, 2)
        self.assertEqual(values, output_values)


if __name__ == '__main__':
    unittest.main()
