from unittest import TestCase
from src.katas.summaryRanges import Solution

class TestSummaryRanges(TestCase):

    def test_example_1(self):
        nums = [0,1,2,4,5,7]
        Output = ["0->2","4->5","7"]
        result = Solution()
        self.assertEqual(result.summaryRanges(nums), Output)
    
    def test_example_2(self):
        nums = [0,2,3,4,6,8,9]
        Output = ["0","2->4","6","8->9"]
        result = Solution()
        self.assertEqual(result.summaryRanges(nums), Output)