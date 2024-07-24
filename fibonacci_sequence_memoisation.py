import unittest

cache = {}

def fibonacci_sequence(nth_number: int) -> int:
    """
    Recursive implementation of the Fibonacci sequence
    
    nth_number - which number in the sequence is asked for
    returning the integer value, minimum nth_number being
    zero

    complexity
        time O(n)
        space O(n)

    In testing with and without the cache the six test cases
    ran 0.003s and 0.001s respectively
    """
    if nth_number in cache:
        return cache[nth_number]

    if nth_number <= 0:
        return 0
    elif nth_number == 1:
        return 1
    
    one_before = fibonacci_sequence(nth_number - 1)
    cache[nth_number - 1] = one_before
    two_before = fibonacci_sequence(nth_number - 2)
    
    return two_before + one_before

class FibonacciSequenceTest(unittest.TestCase):

    def test_first_value(self):
        self.assertEqual(0, fibonacci_sequence(0))

    def test_second_value(self):
        self.assertEqual(1, fibonacci_sequence(1))
    
    def test_third_value(self):
        self.assertEqual(1, fibonacci_sequence(2))

    def test_forth_value(self):
        self.assertEqual(2, fibonacci_sequence(3))

    def test_fifth_value(self):
        self.assertEqual(3, fibonacci_sequence(4))

    def test_19_value(self):
        self.assertEqual(4181, fibonacci_sequence(19))

if __name__ == '__main__':
    unittest.main()
