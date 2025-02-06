from unittest import TestCase
from src.katas.binaryTreePath import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestBinaryTreePaths(TestCase):

    def test_multiple_tree_nodes(self):
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)

        expected = ["1->2->5", "1->3"] 

        result = Solution().binaryTreePaths(root)  

        self.assertCountEqual(result, expected) 
    
    def test_single_tree_node(self):
      
        root = TreeNode(1)
        

        expected = ["1"] 

        result = Solution().binaryTreePaths(root)  

        self.assertCountEqual(result, expected) 