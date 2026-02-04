from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        total = 0
        for x in nums:
            if x in seen:
                duplicate = x
            else:
                seen.add(x)
                total += x


        expected_sum = n * (n + 1) // 2

        missing = expected_sum - total

        return [duplicate, missing]

        