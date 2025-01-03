import unittest

def coin_change(denominations: list[int], amount: int) -> int:
    """
    Returns the lowest of coins for a given amount, amount
    must be a multiple of the lowest denomination which must
    be one
    """

    # build a matrix of values with additional zeros in the first and last row column
    # populate the matrix taking the lowest value of coins used
    # return rightmost value that is furthest down

    matrix = [[0] * (amount + 1) for _ in denominations]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            coin_value = denominations[i - 1]
            if coin_value <= amount and j % coin_value == 0:
                if matrix[i - 1][j - 1] == 0:
                    matrix[i][j] = amount / coin_value
                else:
                    

    return matrix[-1][-1]

class CoinChangeTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
