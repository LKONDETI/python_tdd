from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1Set, nums2Set = set(nums1), set(nums2)
        res = [[], []] 
        
        for num in nums1Set:
            if num not in nums2Set:
                res[0].append(num)
        
        for num in nums2Set:
            if num not in nums1Set:
                res[1].append(num)
        return res