from unittest import TestCase
from src.katas.binaryTreeInorderTraversal import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestBinaryTreeInorderTraversal(TestCase):

    def test_multiple_tree_nodes(self):

        #root = [1,null,2,3]
        Output = [1,3,2]

        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        result = Solution().inorderTraversal(root)

        self.assertEqual(result, Output) 
    
    def test_single_tree_node(self):
        
        #root = [1]
        Output = [1]

        root = TreeNode(1)

        result = Solution().inorderTraversal(root)

        self.assertEqual(result, Output)
