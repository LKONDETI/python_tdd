from unittest import TestCase
from src.katas.isSubquence import Solution

class TestIsSubquence(TestCase):

    def test_example_1(self):
        s = "abc"
        t = "ahbgdc"
        result = Solution()
        self.assertEqual(result.isSubsequence(s,t), True)
    
    def test_example_2(self):
        s = "axc"
        t = "ahbgdc"
        result = Solution()
        self.assertEqual(result.isSubsequence(s,t), False)
    
