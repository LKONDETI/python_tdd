from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(tree1, tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            if tree1.val != tree2.val:
                return False
            return isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)

        if root is None:
            return True
        return isMirror(root.left, root.right)

