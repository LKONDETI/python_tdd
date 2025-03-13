from src.katas.fizzBuzzLeetcode import Solution
from unittest import TestCase


class TestFizzBuzz(TestCase):

    def test_when_n_3(self):
        n = 3
        Output =  ["1","2","Fizz"]
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(n), Output)

    def test_when_n_5(self):
        n = 5
        Output =  ["1","2","Fizz","4","Buzz"]
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(n), Output)
    
    def test_when_n_15(self):
        n = 15
        Output= ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        solution = Solution()
        self.assertEqual(solution.fizzBuzz(n), Output)