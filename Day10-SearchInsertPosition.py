"""
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class SearchInsertPosition:
    def searchInsert1(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = end + ((start - end) // 2)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def searchInsert2(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums) - 1):
                if nums[i] <= target <= nums[i + 1]:
                    return i + 1


obj = SearchInsertPosition()
print(obj.searchInsert1([1, 3, 5, 6], 5))
print(obj.searchInsert2([1, 3, 5, 6], 5))
print(obj.searchInsert1([1, 3, 5, 6], 2))
print(obj.searchInsert2([1, 3, 5, 6], 2))
print(obj.searchInsert1([1, 3, 5, 6], 7))
print(obj.searchInsert2([1, 3, 5, 6], 7))
print(obj.searchInsert1([1, 3, 5, 6], 0))
print(obj.searchInsert2([1, 3, 5, 6], 0))
