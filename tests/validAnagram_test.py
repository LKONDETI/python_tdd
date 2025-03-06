from unittest import TestCase
from src.katas.validAnagram import Solution

class TestValidAnagram(TestCase):

    def test_anagram(self):
        s = "anagram"
        t = "nagaram"
        result = Solution()
        self.assertEqual(result.isAnagram(s,t), True)
    
    def test_car(self):
        s = "car"
        t = "rat"
        result = Solution()
        self.assertEqual(result.isAnagram(s,t), False)