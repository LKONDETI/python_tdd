from unittest import TestCase
from src.katas.lengthOfLastWords import Solution

class TestLengthOfLastWords(TestCase):

    def test_no_of_last_words_in_hello_world(self):
        s = "Hello World"
        result = Solution()
        self.assertEqual(result.lengthOfLastWord(s), 5)
    
    def test_no_of_last_words_in_flyMeToTheMoon(self):
        s = "   fly me   to   the moon  "
        result = Solution()
        self.assertEqual(result.lengthOfLastWord(s), 4)
    
    def test_no_of_last_words_in_luffy_still_joyboy(self):
        s = "luffy is still joyboy"
        result = Solution()
        self.assertEqual(result.lengthOfLastWord(s), 6)
    
