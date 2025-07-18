from unittest import TestCase
from src.katas.deleteNodeInBST import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestDeleteNodeInBS(TestCase):
        
    def serialize(self, root):
        """Serialize tree to list using preorder traversal (None for missing nodes)."""
        if not root:
            return [None]
        return [root.val] + self.serialize(root.left) + self.serialize(root.right)

    def test_multiple_tree_nodes(self):

        #root = [5,3,6,2,4,null,7]
      
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(7)
        key = 3
        #expected = [5,4,6,2,null,null,7]
        expected = TreeNode(5)
        expected.left = TreeNode(4)
        expected.right = TreeNode(6)
        expected.left.left = TreeNode(2)
        expected.right.right = TreeNode(7)


        result = Solution().deleteNode(root, key)  

        self.assertEqual(self.serialize(result), self.serialize(expected))
    
    def test_single_node_tree(self):
        #root = [1]
        root = TreeNode(1)
        key = 1
        expected = None

        result = Solution().deleteNode(root, key)  

        self.assertEqual(result, expected)
    
    def test_no_node_tree(self):
        #root = [5,3,6,2,4,null,7]
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(7)
        key = 0
        expected = TreeNode(5)
        expected.left = TreeNode(3)
        expected.right = TreeNode(6)
        expected.left.left = TreeNode(2)
        expected.left.right = TreeNode(4)
        expected.right.right = TreeNode(7)

        result = Solution().deleteNode(root, key)  

        self.assertEqual(self.serialize(result), self.serialize(expected))
    
    def test_empty_leaf_node(self):
        #root = [1]
        root = []
        key = 0
        expected = []

        result = Solution().deleteNode(root, key)
        self.assertEqual(result, expected)

    