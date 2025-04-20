from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #(i+2) % len(nums) is used to handle the case when k is greater than the length of nums
        # above soln is O(n) and O(n)
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
        