from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]
"""
1. If str1 + str2 is not equal to str2 + str1, return "" (no common divisor exists)
2. Compute gcd_length = GCD(len(str1), len(str2))
3. Return the prefix of str1 with length gcd_length
"""
       