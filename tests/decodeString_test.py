from unittest import TestCase
from src.katas.decodeString import Solution

class TestDecodeString(TestCase):

    def test_single_item(self):
        s = "3[a]2[bc]"
        result = Solution()
        self.assertEqual(result.decodeString(s), "aaabcbc")
    
    def test_single_item_with_nested_items(self):
        s = "3[a2[c]]"
        result = Solution()
        self.assertEqual(result.decodeString(s), "accaccacc")
    
    def test_multiple_items(self):
        s = "2[abc]3[cd]ef"
        result = Solution()
        self.assertEqual(result.decodeString(s), "abcabccdcdcdef")