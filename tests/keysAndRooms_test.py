from src.katas.keysAndRooms import Solution
from unittest import TestCase


class TestKeysAndRooms(TestCase):

    def test_example_1(self):
        rooms = [[1],[2],[3],[]]
        solution = Solution()
        self.assertEqual(solution.canVisitAllRooms(rooms), True)
    
    def test_example_2(self):
        rooms = [[1,3],[3,0,1],[2],[0]]
        solution = Solution()
        self.assertEqual(solution.canVisitAllRooms(rooms), False)
    
    def test_example_3(self):
        rooms = [[1,2],[2,3],[3],[]]
        solution = Solution()
        self.assertEqual(solution.canVisitAllRooms(rooms), True)