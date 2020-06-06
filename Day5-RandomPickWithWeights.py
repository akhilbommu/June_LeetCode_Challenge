"""
https://leetcode.com/problems/random-pick-with-weight/
"""
from typing import List
import random


class RandomPickWithWeights:
    def __init__(self, w: List[int]):
        self.prefix_sum = []
        sum_till_now = 0
        for weight in w:
            sum_till_now += weight
            self.prefix_sum.append(sum_till_now)
        self.total_sum = sum_till_now

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        """
        for i in range(len(self.prefix_sum)):
            if self.prefix_sum[i] > random_num:
                return i
        """
        low, high = 0, len(self.prefix_sum)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix_sum[mid]:
                low = mid + 1
            else:
                high = mid
        return low


obj = RandomPickWithWeights([1, 3])
print(obj.pickIndex())
print(obj.pickIndex())
