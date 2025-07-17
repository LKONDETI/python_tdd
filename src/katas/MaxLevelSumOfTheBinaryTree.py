class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        max_sum = root.val
        max_level = 1
        current_level = 1

        while queue:
            level_sum = 0
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            current_level += 1
        return max_level


        