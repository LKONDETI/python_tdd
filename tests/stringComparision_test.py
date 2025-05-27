from unittest import TestCase
from src.katas.stringComparision import Solution

class TestStringComparision(TestCase):

    def test_example_1(self):
        chars = ["a","a","b","b","c","c","c"]
        
        result = Solution()
        
        self.assertEqual(result.compress(chars), 6)

    def test_example_2(self):
        chars = ["a"]
        
        result = Solution()
        
        self.assertEqual(result.compress(chars), 1)
    
    def test_example_3(self):
        chars = ["a","b","b","b","b","b","b","b"]
        
        result = Solution()
        
        self.assertEqual(result.compress(chars), 4)


    