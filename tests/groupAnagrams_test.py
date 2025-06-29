from unittest import TestCase
from src.katas.groupAnagrams import Solution

class TestGroupAnagrams(TestCase):

    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = Solution()
        self.assertEqual(result.groupAnagrams(strs), [["bat"],["nat","tan"],["ate","eat","tea"]])
    
    def test_example_2(self):
        strs = [""]
        result = Solution()
        self.assertEqual(result.groupAnagrams(strs), [[""]])
    
    def test_example_3(self):
        strs = ["a"]
        result = Solution()
        self.assertEqual(result.groupAnagrams(strs), [["a"]])