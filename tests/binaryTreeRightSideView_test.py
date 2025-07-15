from unittest import TestCase
from src.katas.binaryTreeRightSideView import Solution

class TreeNode:
  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestBinaryTreeRightSideView(TestCase):

    def test_multiple_tree_nodes(self):

        #root = [1,2,3,null,5,null,4]
      
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)

        expected = [1,3,4]

        result = Solution().rightSideView(root)  

        self.assertEqual(result, expected) 
    
    def test_single_node(self):
        
            #root = [1]
            root = TreeNode(1)
    
            expected = [1]
    
            result = Solution().rightSideView(root)  
    
            self.assertEqual(result, expected)
    
    def test_more_left_nodes(self):
         #root = [1,2,3,4,null,null,null,5]
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        expected = [1, 3, 4, 5]
        result = Solution().rightSideView(root)
        self.assertEqual(result, expected)
