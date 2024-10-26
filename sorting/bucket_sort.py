import unittest

from sort_utils import is_sorted


def bucket_sort(values: float) -> list[float]:
    """
    Bucket sort implementation, create buckets to divide the values into, each bucket is then
    sorted by a sorting algorithm (insertion sort), the output list is then created by adding the
    values from each ordered bucket.

    Not in place, used on numbers from 0-0.99 inclusive

    complexity
        time:

        space:
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


def insertion_sort(values: float) -> None:
    return values


class BucketSortTest(unittest.TestCase):

    def test_even_distribution_worst_case(self):
        values = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
        output_values = bucket_sort(values)
        self.assertEqual(len(values), len(output_values))
        self.assertTrue(is_sorted(output_values))


if __name__ == '__main__':
    unittest.main()
