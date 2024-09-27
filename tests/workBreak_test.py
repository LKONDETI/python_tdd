from unittest import TestCase
from src.katas.wordBreak import Solution

class TestWorkBreak(TestCase):

    def test_leetcode(self):
        s = "leetcode"
        wordDict = ["leet","code"]
        result = Solution()
        check = result.wordBreak(s, wordDict)
        output = True
        self.assertEqual(check, output)
    
    def test_AppleNApple(self):
        s = "applepenapple"
        wordDict = ["apple","pen"]
        result = Solution()
        check = result.wordBreak(s, wordDict)
        output = True
        self.assertEqual(check, output)
    
    def test_Cats_N_Dog(self):
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        result = Solution()
        check = result.wordBreak(s, wordDict)
        output = False
        self.assertEqual(check, output)
    


    

    