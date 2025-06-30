from unittest import TestCase
from src.katas.IntToRoman import Solution

class TestIntToRoman(TestCase):

    def test_example_1(self):
        num = 3749
        result = Solution()
        self.assertEqual(result.intToRoman(num), "MMMDCCXLIX")
    
    def test_example_2(self):
        num = 58
        result = Solution()
        self.assertEqual(result.intToRoman(num), "LVIII")
    
    def test_example_3(self):
        num = 1994
        result = Solution()
        self.assertEqual(result.intToRoman(num), "MCMXCIV")
    