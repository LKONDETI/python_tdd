from unittest import TestCase
from src.katas.MaxLevelSumOfTheBinaryTree import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestMaxLevelSumOfTheBinaryTree(TestCase):

    def test_multiple_tree_nodes(self):

        #root = [1,7,0,7,-8,null,null]
      
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)

        result = Solution().maxLevelSum(root)  

        self.assertEqual(result, 2)
    
    def test_multiple_tree_nodes(self):

        #root = [1,7,0,7,-8,null,null]
      
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)

        result = Solution().maxLevelSum(root)  
        self.assertEqual(result, 2)
    
    def test_single_node_tree(self):
        root = TreeNode(5)
        result = Solution().maxLevelSum(root)
        self.assertEqual(result, 1)
    
    def test_huge_number_nodes_tree(self):
        #root = [989,null,10250,98693,-89388,null,null,null,-32127]
        root = TreeNode(989)
        root.right = TreeNode(10250)
        root.right.left = TreeNode(98693)
        root.right.right = TreeNode(-89388)
        root.right.right.right = TreeNode(-32127)
        result = Solution().maxLevelSum(root)
        self.assertEqual(result, 2)
    
