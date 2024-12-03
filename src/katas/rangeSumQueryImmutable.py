from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0
        for n in nums:
            curr += n
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum     
