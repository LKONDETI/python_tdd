from unittest import TestCase
from src.katas.binaryTreeMaximumPathSum import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestBinaryTreeMaximumPathSum(TestCase):

    def test_three_tree_nodes(self):

        #root = [1,2,3]
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        result = Solution().maxPathSum(root)  

        self.assertEqual(result, 6) 
    
    def test_negitive_nodes(self):
      
      #root = [-10,9,20,null,null,15,7]
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        result = Solution().maxPathSum(root)  

        self.assertEqual(result, 42) 