from src.katas.shuffleTheArray import Solution
from unittest import TestCase


class TestShuffleTheArray(TestCase):

    def test_case1(self):
        nums = [2,5,1,3,4,7]
        n = 3
        solution = Solution()
        self.assertEqual(solution.shuffle(nums,n), [2,3,5,4,1,7] )
    
    def test_case2(self):
        nums = [1,2,3,4,4,3,2,1]
        n = 4
        solution = Solution()
        self.assertEqual(solution.shuffle(nums,n), [1,4,2,3,3,2,4,1] )
    
    def test_case3(self):
        nums = [1,1,2,2]
        n = 2
        solution = Solution()
        self.assertEqual(solution.shuffle(nums,n), [1,2,1,2] )
    
