from unittest import TestCase
from src.katas.courseSchedule import Solution

class TestCourseSchedule(TestCase):

    def test_case1(self):
        numCourses = 2
        prerequisites = [[1,0]]
        result = Solution()
        self.assertEqual(result.findOrder(numCourses,prerequisites), True)

    def test_case2(self):
        numCourses = 2
        prerequisites = [[1,0],[0,1]]
        result = Solution()
        self.assertEqual(result.findOrder(numCourses,prerequisites), False)