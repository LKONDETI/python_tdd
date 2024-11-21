from unittest import TestCase
from src.katas.firstUniqueCharacterInString import Solution

class TestFirstUniqueCharaterString(TestCase):

    def test_leetcode(self):
        s = "leetcode"
        result = Solution()
        self.assertEqual(result.firstUniqChar(s), 0)
    
    def test_loveleetcode(self):
        s = "loveleetcode"
        result = Solution()
        self.assertEqual(result.firstUniqChar(s), 2)

    def test_aabb(self):
        s = "aabb"
        result = Solution()
        self.assertEqual(result.firstUniqChar(s), -1)