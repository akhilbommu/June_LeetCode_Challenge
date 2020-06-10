"""
https://leetcode.com/problems/is-subsequence/
"""


class IsSubsequence:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        if s_index == len(s):
            return True
        return False

obj = IsSubsequence()
print(obj.isSubsequence("abc", "ahbgdc"))
print(obj.isSubsequence("axc", "ahbgdc"))