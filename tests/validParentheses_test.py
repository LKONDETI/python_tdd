from unittest import TestCase
from src.katas.validParentheses import Solution

class TestValidParenthses(TestCase):

    def test_case1(self):
        s = "()"
        result = Solution()
        self.assertEqual(result.isValid(s),True)
    
    def test_case2(self):
        s = "()[]{}"
        result = Solution()
        self.assertEqual(result.isValid(s),True)
    
    def test_case3(self):
        s = "(]"
        result = Solution()
        self.assertEqual(result.isValid(s),False)
    
    def test_case4(self):
        s = "([])"
        result = Solution()
        self.assertEqual(result.isValid(s),True)