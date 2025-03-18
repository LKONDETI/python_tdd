class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0,0
        while i < len(s) and j <len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        """
        1. Initialize two pointers: `i = 0` for `s` and `j = 0` for `t`
2. While `i < length of s` and `j < length of t`:
    a. If `s[i] == t[j]`, move `i` to the next character in `s`
    b. Always move `j` to the next character in `t`
3. If `i == length of s`, return True (all characters in `s` were found in `t` in order)
4. Otherwise, return False
"""
       