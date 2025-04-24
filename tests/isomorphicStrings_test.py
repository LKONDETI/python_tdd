from unittest import TestCase
from src.katas.isomorphicStrings import Solution

class TestIsomorphicStrings(TestCase):

    def test_example_1(self):
        s = "egg"
        t = "add"
        result = Solution()
        self.assertEqual(result.isIsomorphic(s,t), True)
    
    def test_example_2(self):
        s = "foo"
        t = "bar"
        result = Solution()
        self.assertEqual(result.isIsomorphic(s,t), False)
    
    def test_example_3(self):
        s = "paper"
        t = "title"
        result = Solution()
        self.assertEqual(result.isIsomorphic(s,t), True)