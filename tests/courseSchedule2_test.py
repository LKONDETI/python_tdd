from unittest import TestCase
from src.katas.courseSchedule2 import Solution

class TestCourseSchedule(TestCase):

    def test_two_courses(self):
        numCourses = 2
        prerequisites = [[1,0]]
        output = [0,1]
        result = Solution()
        self.assertEqual(result.findOrder(numCourses,prerequisites), output)

    def test_multiple_course(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        output = [0,1,2,3]
        result = Solution()
        self.assertEqual(result.findOrder(numCourses,prerequisites), output)
    
    def test_empty_course(self):
        numCourses = 1
        prerequisites = []
        output = [0]
        result = Solution()
        self.assertEqual(result.findOrder(numCourses,prerequisites), output)
    
