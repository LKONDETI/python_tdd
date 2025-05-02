from unittest import TestCase
from src.katas.searchInBinaryTree import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSearchInBinaryTree(TestCase):
    
    def test_multiple_node_list(self):
        # Create the test tree:
        #      4
        #    /   \
        #   2     7
        #  / \
        # 1   3
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        
        val = 2
        expected_output = [2, 1, 3]
        
        # Call the searchBST function
        result = Solution().searchBST(root, val)
        
        # Convert the resulting subtree to a list for comparison
        self.assertEqual(self.get_values(result), expected_output)
    def test_single_node(self):
        # Create a single node tree
        root = TreeNode(1)
        val = 1
        expected_output = [1]
        
        # Call the searchBST function
        result = Solution().searchBST(root, val)
        
        # Convert the resulting subtree to a list for comparison
        self.assertEqual(self.get_values(result), expected_output)
    
    def test_non_existent_value(self):
        # Create the test tree:
        #      4
        #    /   \
        #   2     7
        #  / \
        # 1   3
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        
        val = 5
        expected_output = []
        
        # Call the searchBST function
        result = Solution().searchBST(root, val)
        
        # Convert the resulting subtree to a list for comparison
        self.assertEqual(self.get_values(result), expected_output)
    
    def get_values(self, node):
        """Convert a tree to a list using in-order traversal"""
        if not node:
            return []
        
        values = []
        # In-order traversal: left, root, right
        values.append(node.val)
        values.extend(self.get_values(node.left))
        values.extend(self.get_values(node.right))
        
        return values