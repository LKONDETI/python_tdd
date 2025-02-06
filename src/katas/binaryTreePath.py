
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def traverse(node, pathTillCurNode):
            if not (node.left or node.right):
                paths.append( "->".join(pathTillCurNode))
                return
            if node.left:
                traverse(node.left, pathTillCurNode + (str(node.left.val)))
            if node.right:
                traverse(node.right, pathTillCurNode + (str(node.right.val)))

        paths = []
        traverse(root, [str(root.val)])
        return paths

      