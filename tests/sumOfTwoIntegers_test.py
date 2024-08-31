from src.katas.sumOfTwoIntegers import Solution
from unittest import TestCase


class TestSumOfTwoIntegers(TestCase):

    def test_resultant_Five(self):
        
        solution = Solution()
        self.assertEqual(solution.getSum(2,3), 5)

    def test_resultant_Three(self):
        
        solution = Solution()
        self.assertEqual(solution.getSum(1,2), 3)
    
    def test_resultant_Double_Digits(self):
        
        solution = Solution()
        self.assertEqual(solution.getSum(25,41), 66)