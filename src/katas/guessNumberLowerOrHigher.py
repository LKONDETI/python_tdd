# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int, pick: int) -> int:
        def guess(num: int) -> int:
            if num > pick:
                return -1
            elif num < pick:
                return 1
            else:
                return 0

        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1
# The function guessNumber uses binary search to find the picked number. time complexity is O(log n) and space complexity is O(1).
