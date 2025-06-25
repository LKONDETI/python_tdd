class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left , right = 1, x
        while left <= right:
            mid = (left + right)//2
            if mid * mid ==x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
        # Time complexity: O(log n) and Space complexity: O(1)