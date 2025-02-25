class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List        
class Solution:

    def helper(self, root, targetSum, lst, result):
        if root.left is None and root.right is None:
            if root.val == targetSum:
                result += [lst + [root.val]]
        
        if root.left:
            self.helper(root.left, targetSum - root.val, lst +[root.val], result)
        
        if root.right:
            self.helper(root.right, targetSum - root.val, lst +[root.val], result)

        return result


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        return self.helper(root,targetSum, [], [])


#space and time : O(n)