from unittest import TestCase
from src.katas.romanAndInteger import Solution

class TestRomanAndInteger(TestCase):

    def test_number_3(self):
        s = "III"
        result = Solution()
        self.assertEqual(result.romanToInt(s), 3)
    
    def test_number_58(self):
        s = "LVIII"
        result = Solution()
        self.assertEqual(result.romanToInt(s), 58)
    
    def test_number_1994(self):
        s = "MCMXCIV"
        result = Solution()
        self.assertEqual(result.romanToInt(s), 1994)