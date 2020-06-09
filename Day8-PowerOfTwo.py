"""
https://leetcode.com/problems/power-of-two/
"""


class PowerOfTwo:
    def isPowerOfTwo1(self, n: int) -> bool:
        power = 1
        while power < n:
            power *= 2
        return power == n

    def isPowerOfTwo2(self, n: int) -> bool:
        binary_num = bin(n)[2:]
        return binary_num[0] == '1' and binary_num.count('1') == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        return n > 0 and n & n - 1 == 0


obj = PowerOfTwo()
print(obj.isPowerOfTwo1(1))
print(obj.isPowerOfTwo2(1))
print(obj.isPowerOfTwo3(1))
print(obj.isPowerOfTwo1(16))
print(obj.isPowerOfTwo2(16))
print(obj.isPowerOfTwo3(16))
print(obj.isPowerOfTwo1(218))
print(obj.isPowerOfTwo2(218))
print(obj.isPowerOfTwo3(218))