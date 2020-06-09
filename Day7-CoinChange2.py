"""
https://leetcode.com/problems/coin-change-2/
"""
from typing import List


class CoinChange:
    def change(self, amount: int, coins: List[int]) -> int:
        dp_list = [0] * (amount + 1)
        dp_list[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp_list[x] += dp_list[x - coin]
        return dp_list[amount]


obj = CoinChange()
print(obj.change(5, [1, 2, 5]))
print(obj.change(3, [2]))
print(obj.change(10, [10]))
