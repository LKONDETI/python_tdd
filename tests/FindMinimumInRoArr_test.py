from src.katas import findMinimumInRoArr
import unittest


class TestFindMinimumInRoArr(unittest.TestCase):

    def test_five_elements_array(self):
        nums = [3,4,5,1,2]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (1))

    def test_seven_elements_array(self):
        nums = [4,5,6,7,0,1,2]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (0))

    def test_four_elements_array(self):
        nums = [11,13,15,17]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (11)) 

    def test_negetive_elements_array(self):
        nums = [-11,0,-3,9,-2]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (-11))

    def test_eleven_elements_array(self):
        nums = [-1,0,-3,9,-2,5,2,1,7,-8,-10]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (-10))

    def test_four_negetive_elements_array(self):
        nums = [-11,-13,-15,-17]
        solution = findMinimumInRoArr.FindMin()
        result = solution.find_min_in_rotated_array(nums)
        self.assertEqual(result, (-17))    