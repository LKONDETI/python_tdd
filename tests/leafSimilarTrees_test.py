from unittest import TestCase
from src.katas.leafSimilarTrees import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestLeafSimilarTrees(TestCase):

    def test_example1(self):

        #root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
        
      
        root1 = TreeNode(3)
        root1.left = TreeNode(5)
        root1.right = TreeNode(1)
        root1.left.left = TreeNode(6)
        root1.left.right = TreeNode(2)
        root1.right.left = TreeNode(9)
        root1.right.right = TreeNode(8)
        root1.left.right.left = TreeNode(7)
        root1.left.right.right = TreeNode(4)
        root2 = TreeNode(3)
        root2.left = TreeNode(5)
        root2.right = TreeNode(1)
        root2.left.left = TreeNode(6)
        root2.left.right = TreeNode(7)
        root2.right.left = TreeNode(4)
        root2.right.right = TreeNode(2)
        root2.right.right.left = TreeNode(9)
        root2.right.right.right = TreeNode(8)
        output = True

        result = Solution().leafSimilar(root1, root2)  

        self.assertEqual(result, output)

    def test_example2(self):
        #root1 = [1,2,3], root2 = [1,3,2]
        
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root2 = TreeNode(1)
        root2.left = TreeNode(3)
        root2.right = TreeNode(2)
        output = False

        result = Solution().leafSimilar(root1, root2)  

        self.assertEqual(result, output)
