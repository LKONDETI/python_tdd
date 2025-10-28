from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            # If current number is not consecutive, close the range
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
        
        # Add the final range
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")
        
        return res
