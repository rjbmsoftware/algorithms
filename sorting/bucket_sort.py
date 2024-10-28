import unittest

from sort_utils import is_sorted
from insertion_sort import insertion_sort


def bucket_sort(values: float) -> list[float]:
    """
    Bucket sort implementation, create buckets to divide the values into, each bucket is then
    sorted by a sorting algorithm (insertion sort), the output list is then created by adding the
    values from each ordered bucket.

    Not in place, used on numbers from 0-0.99 inclusive.

    The advantage of bucket sort is the buckets can be sorted separately allowing them to be sorted
    by another processor, it could also be used for very large data sets that will not fit into
    memory.

    complexity
        time:
            O(n + (sorting algorithm)) where n is the number of elements as each element will be
            visited once to divide the values between the buckets
        space:
            O(n + (sorting algorithm)) where n is the number of elements as each will be stored in
            the relevant bucket
    """
    buckets = [[] for _ in range(10)]
    for value in values:
        bucket_index = int(value * 10)
        buckets[bucket_index].append(value)

    output_list = []

    for bucket in buckets:
        insertion_sort(bucket)
        output_list.extend(bucket)

    return output_list


class BucketSortTest(unittest.TestCase):

    def test_even_distribution_worst_case(self):
        values = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
        output_values = bucket_sort(values)
        self.assertEqual(len(values), len(output_values))
        self.assertTrue(is_sorted(output_values))

    def test_buckets_are_sorted(self):
        values = [0.19, 0.18, 0.17, 0.16, 0.15]
        output_values = bucket_sort(values)
        self.assertEqual(output_values, [0.15, 0.16, 0.17, 0.18, 0.19])

    def test_empty_is_sorted(self):
        values = []
        output_values = bucket_sort(values)
        self.assertFalse(output_values)

    def test_single_value_is_sorted(self):
        values = [0.1]
        output_values = bucket_sort(values)
        self.assertEqual(values, output_values)


if __name__ == '__main__':
    unittest.main()
