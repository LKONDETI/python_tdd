from unittest import TestCase
from src.katas.pathSum3 import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestPathSum3(TestCase):

    def test_target_sum_8(self):

        #root = [10,5,-3,3,2,null,11,3,-2,null,1]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        targetSum = 8

        output = 3

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output) 

    def test_target_sum_0(self):
        
        #root = [10,5,-3,3,2,null,11,3,-2,null,1]
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(2)
        root.right.right = TreeNode(11)
        root.left.left.left = TreeNode(3)
        root.left.left.right = TreeNode(-2)
        root.left.right.right = TreeNode(1)
        targetSum = 0

        output = 0

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output)
    
    def test_multiple_tree_nodes(self):

        #root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
      
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

        output = 3

        result = Solution()  

        self.assertEqual(result.pathSum(root, targetSum), output) 
    


