from src.katas.uniqueNoOfOccurances import Solution
from unittest import TestCase


class TestUniqueNoOfOccurances(TestCase):

    def test_positive_integers(self):
        arr = [1,2,2,1,1,3]
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), True)
    
    def test_positive_integers_with_equal_occurances(self):
        arr = [1,2]
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), False)
    
    def test_negative_integers(self):
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        solution = Solution()
        self.assertEqual(solution.uniqueOccurrences(arr), True)
    

   