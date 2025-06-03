from unittest import TestCase
from src.katas.maxDepthBinaryTree import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestMaxDepthofBinaryTree(TestCase):

    def test_multiple_tree_nodes(self):

        #root = [3,9,20,null,null,15,7]
        Output = 3
      
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        result = Solution().maxDepth(root)  

        self.assertEqual(result, Output)
    
    def test_single_tree_node(self):
        #root = [1]
        Output = 1
        
        root = TreeNode(1)

        result = Solution().maxDepth(root)  

        self.assertEqual(result, Output)
    
    def test_double_level_tree(self):
        #root = [1,null,2]
        Output = 2
        
        root = TreeNode(1)
        root.right = TreeNode(2)

        result = Solution().maxDepth(root)  

        self.assertEqual(result, Output)