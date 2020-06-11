"""
https://leetcode.com/problems/sort-colors/submissions/
"""
from typing import List


class SortColors:
    def sortColors1(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def sortColors2(self, nums: List[int]) -> None:
        start, end, index = 0, len(nums) - 1, 0
        while index <= end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start, index = start + 1, index + 1
            elif nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            else:
                index += 1
        return nums


obj = SortColors()
print(obj.sortColors1([2, 0, 2, 1, 1, 0]))
print(obj.sortColors2([2, 0, 2, 1, 1, 0]))
