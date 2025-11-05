from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 0          # number of jumps used so far
        current_end = 0    # end of the current jump range
        farthest = 0       # farthest index we can reach from current range

            # We iterate only up to len(nums) - 2 because
            # when we reach the last index, we don't need to jump anymore.
        for i in range(len(nums) - 1):
                # Update the farthest we can reach from any index in this range
            farthest = max(farthest, i + nums[i])

                # If we've reached the end of the current range,
                # we must do another jump.
            if i == current_end:
                jumps += 1
                current_end = farthest

                    # Optional early stop: if current_end already reaches the end
            if current_end >= len(nums) - 1:
                break

        return jumps