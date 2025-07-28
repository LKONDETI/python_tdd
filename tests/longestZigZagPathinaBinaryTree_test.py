from unittest import TestCase
from src.katas.longestZigZagPathinaBinaryTree import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestLongestZigZagPathinaBinaryTree(TestCase):

    def test_example_1(self):

        #root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
        
        root = TreeNode(1)
        root.right = TreeNode(1)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(1)
        root.right.right.left = TreeNode(1)
        root.right.right.right = TreeNode(1)
        root.right.right.left.right = TreeNode(1)
        root.right.right.left.right.right = TreeNode(1)
       


        result = Solution().longestZigZag(root)  

        self.assertEqual(result, 3) 
    
    def test_example_2(self):
        
        #root = [1,1,1,null,1,null,null,1,1,null,1]
        
        root = TreeNode(1)
        root.left = TreeNode(1)
        root.right = TreeNode(1)
        root.left.right = TreeNode(1)
        root.left.right.left = TreeNode(1)
        root.left.right.right = TreeNode(1)
        root.left.right.left.right = TreeNode(1)

        result = Solution().longestZigZag(root)  

        self.assertEqual(result, 4)