from src.katas import searchInRotatedArray
import unittest


class TestSearchInRotatedArray(unittest.TestCase):

    def test_1(self):
        nums = [4,5,6,7,0,1,2]
        solution = searchInRotatedArray.Solution()
        self.assertEqual(solution.search(nums, 0), 4)
        