"""
https://leetcode.com/problems/largest-divisible-subset/
"""
from typing import List


class LargestDivisibleSubset:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums = sorted(nums)
        result_list = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(result_list[i]) < len(result_list[j]) + 1:
                    result_list[i] = result_list[j] + [nums[i]]

        return max(result_list, key=len)


obj = LargestDivisibleSubset()
print(obj.largestDivisibleSubset([1, 2, 3]))
print(obj.largestDivisibleSubset([1, 2, 4, 8]))
