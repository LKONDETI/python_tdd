from typing import List
from functools import lru_cache

#time complexity: O(2 * target * n) = O(target * n)
#space complexity: O(target * n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 != 0:  
            return False
        target = tot // 2

        @lru_cache(None)  # Memoization
        def dp(i, amt):
            if amt == target:  
                return True
            if i >= len(nums) or amt > target:  
                return False

            
            return dp(i + 1, amt + nums[i]) or dp(i + 1, amt)

        return dp(0, 0)
        