import unittest

def coin_change(denominations: list[int], amount: int) -> int:
    """
    Returns the lowest of coins for a given amount, amount
    must be a multiple of the lowest denomination which must
    be one
    """

    matrix = [[0] * (amount + 1) for _ in range(len(denominations) + 1)]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            coin_value = denominations[i - 1]
            if coin_value <= j:
                remainder = j % coin_value
                if remainder == 0:
                    if matrix[i - 1][j - 1] == 0:
                        matrix[i][j] = j / coin_value
                    else:
                        coins_used = j // coin_value + matrix[i][remainder]
                        if matrix[i - 1][j] > coins_used:
                            matrix[i][j] = coins_used
                        else:
                            matrix[i][j] = matrix[i - 1][j]
                else:
                    coins_used = j // coin_value + matrix[i][remainder]
                    if matrix[i - 1][j] > coins_used:
                        matrix[i][j] = coins_used
                    else:
                        matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = matrix[i - 1][j]

    return matrix[-1][-1]

class CoinChangeTest(unittest.TestCase):

    def test_single_coin(self):
        coins = [1]
        coins_used = coin_change(coins, 5)
        self.assertEqual(coins_used, 5)

    def test_two_differing_denominations(self):
        coins = [1, 2]
        coins_used = coin_change(coins, 3)
        self.assertEqual(coins_used, 2)

    def test_largest_denomination_uses_the_least_coins(self):
        coins = [1, 2, 3]
        coins_used = coin_change(coins, 3)
        self.assertEqual(coins_used, 1)

if __name__ == '__main__':
    unittest.main()
