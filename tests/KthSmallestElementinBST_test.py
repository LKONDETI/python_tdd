from unittest import TestCase
from src.katas.KthSmallestElementinBST import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestKthSmallestElementinBST(TestCase):

    def test_five_tree_nodes(self):

        #oot = [3,1,4,null,2], k = 1
      
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        k = 1

        result = Solution()  

        self.assertEqual(result.kthSmallest(root, k), 1) 
    
    def test_multiple_tree_node(self):
      
      #root = [5,3,6,2,4,null,null,1], k = 3
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(2)
        root.left.left.left = TreeNode(1)
        k = 3

        result = Solution()  

        self.assertEqual(result.kthSmallest(root, k), 3) 