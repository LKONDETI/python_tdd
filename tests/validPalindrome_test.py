from unittest import TestCase
from src.katas.validPalindrome import Solution

class TestValidPalindrome(TestCase):

    def test_sentence(self):
        s = "A man, a plan, a canal: Panama"
        result = Solution()
        self.assertEqual(result.isPalindrome(s), True)
    
    def test_False_sentence(self):
        s = "race a car"
        result = Solution()
        self.assertEqual(result.isPalindrome(s), False)
    
    def test_empty_string(self):
       s = " "
       result = Solution()
       self.assertEqual(result.isPalindrome(s), True)
    
