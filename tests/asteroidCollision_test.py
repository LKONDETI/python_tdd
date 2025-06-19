from unittest import TestCase
from src.katas.asteroidCollision import Solution

class TestAsteroidCollision(TestCase):

    def test_double_item_stack(self):
        asteroids = [5,10,-5]
        result = Solution()
        self.assertEqual(result.asteroidCollision(asteroids), [5,10])
    
    def test_empty_stack(self):
        asteroids = [8,-8]
        result = Solution()
        self.assertEqual(result.asteroidCollision(asteroids), [])
    
    def test_single_stack(self):
        asteroids = [10,2,-5]
        result = Solution()
        self.assertEqual(result.asteroidCollision(asteroids), [10])