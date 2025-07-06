from unittest import TestCase
from src.katas.countGoodNodesInBinaryTree import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestCountGoodNodesInBinaryTree(TestCase):

    def test_example1(self):

        #root = [3,1,4,3,null,1,5]
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.left = TreeNode(3)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(5)

        result = Solution().goodNodes(root)  

        self.assertEqual(result, 4) 
    
    def test_example2(self):
        
        #root = [3,3,null,4,2]
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(2)

        result = Solution().goodNodes(root)  

        self.assertCountEqual(result, 3)
    
    