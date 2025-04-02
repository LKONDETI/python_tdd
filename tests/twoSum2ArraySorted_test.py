from src.katas.twoSum2ArraySorted import Solution
from unittest import TestCase


class TesttTwoSum2ArraySorted(TestCase):
    
    def test_example_1(self):
        numbers = [2,7,11,15]
        target = 9
        solution = Solution()
        self.assertEqual(solution.twoSum(numbers, target), [1,2])
    
    def test_example_2(self):
        numbers = [2,3,4]
        target = 6
        solution = Solution()
        self.assertEqual(solution.twoSum(numbers), [1,3])
    
    def test_example_3(self):
        numbers = [-1,0]
        target = -1
        solution = Solution()
        self.assertEqual(solution.twoSum(numbers, -1), [1,2])