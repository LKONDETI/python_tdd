class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional      
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathSumFrom(node, target):
            if node is None:
                return 0
            count = 0
            if node.val == target:
                count += 1
            count += pathSumFrom(node.left, target - node.val)
            count += pathSumFrom(node.right, target - node.val)
            return count

        if root is None:
            return 0

        return (
            pathSumFrom(root, targetSum) +
            self.pathSum(root.left, targetSum) +
            self.pathSum(root.right, targetSum)
        )
