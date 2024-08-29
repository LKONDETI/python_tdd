# python -m unittest tests/searchInRotatedArray_test.py
# tested in bash terminal as it is getting trouble running in the vscode terminal in recognizing 'src.katas.'

from src.katas.searchInRotatedArray import Solution
from unittest import TestCase


class TestSearchInRotatedArray(TestCase):

    def test_searchOf0(self):
        nums = [4,5,6,7,0,1,2]
        solution = Solution()
        self.assertEqual(solution.search(nums, 0), 4)

    def test_searchOf4(self):
        nums = [4,5,6,7,0,1,2]
        solution = Solution()
        self.assertEqual(solution.search(nums, 4), 0)
    
    def test_searchInSingleArray(self):
        nums = [1]
        solution = Solution()
        self.assertEqual(solution.search(nums, 0), -1)

    def test_searchOf3(self):
        nums = [4,5,6,7,0,1,2]
        solution = Solution()
        self.assertEqual(solution.search(nums, 3), -1)
        