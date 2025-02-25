from unittest import TestCase
from src.katas.pathSum2 import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestPathSum2(TestCase):

    def test_multiple_tree_nodes(self):

        #root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22, Output: [[5,4,11,2],[5,8,4,5]]
      
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        targetSum = 22

        output = [[5,4,11,2],[5,8,4,5]]

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output) 
    

    def test_three_tree_nodes(self):

        #root = [1,2,3], targetSum = 5, Output: []
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        targetSum = 5
        output = [ ]

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output) 
    

    def test_double_tree_nodes(self):

        #root = [1,2], targetSum = 0, Output: []
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        
        targetSum = 0
        output = [ ]

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output) 

