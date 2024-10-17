import unittest

def counting_sort(values: list) -> list:
    """
    counting sort positive integer value implementation

    stable sort

    complexity
        time:

        space
    """
    # count the values
    # add the previous value to the current one
    # shift the values to the right removing the end count since we don't need it and the
    # space created is set to zero



def determine_maximum_value(values: list[int]) -> int:
    """
    Deliberately not using max to show complexity
    """
    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value

    return maximum


class CountingSortTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
