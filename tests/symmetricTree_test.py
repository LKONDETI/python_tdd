from unittest import TestCase
from src.katas.symmetricTree import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestLeafSimilarTrees(TestCase):

    def test_example1(self):

        #root = [1,2,2,3,4,4,3]
        
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

 
        output = True

        result = Solution().isSymmetric(root)  

        self.assertEqual(result, output)
    
    def test_example2(self):
        #root = [1,2,2,None,3,None,3]
        
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)

        output = False

        result = Solution().isSymmetric(root)  

        self.assertEqual(result, output)
