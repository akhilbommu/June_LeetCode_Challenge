"""
https://leetcode.com/problems/reverse-string/
"""
from typing import List


class ReverseString:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while (start < end):
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s


obj = ReverseString()
print(obj.reverseString(["h", "e", "l", "l", "o"]))
print(obj.reverseString(["H", "a", "n", "n", "a", "h"]))
