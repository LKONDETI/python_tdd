# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from src.katas import twoSum
import unittest
import array
import random
import time
import numpy as np

class TwoSum_test(unittest.TestCase):
    def test_TwoSum(self):
        solution=  twoSum.TwoSum()
        start_time_millis = int(round( time.time_ns()))
        self.assertEqual(solution.twoSum([2,7,11,15], 9), [0,1])
        # testInt=[-8, 57, 28, 37, 10, 51, 53, 46, 84, 66, 18, 69, 47, 5, 61, 54, 93, 99, 70, 38, 88, 16, 64, 62, 21, 87, 78, 30, 97, 32, 94, 17, 73, 27, 85, 35, 74, 90, 80, 24, 56, 43, 83, 44, 79, 60, 48, 45, 25, 41, 40, 76, 31, 22, 71, 55, 3, 4, 33, 15, 52, 95, 50, 26, 9, 14, 68, 7, 20, 67, 1, 6, 63, 96, 82, 59, 58, 72, 92, 81, 36, 77, 2, 12, 75, 39, 49, -42, 91, 89, 86, 23, 34, 65, 29, 11, 13, 98, 19]
        testInt=np.loadtxt("test1.txt", dtype=int)

        testInt1 = list(set(testInt))
        print("input is:",testInt1)

        self.assertEqual(solution.twoSum(testInt1, 5), [0,3])
        
        end_time_millis = int(round( time.time_ns()))
        print("total time taken in ns:", end_time_millis-start_time_millis)
        # self.assertEqual(solution.twoSum([3,2,4], 6), [1,2])
        # self.assertEqual(solution.twoSum([3,3], 6), [0,1])
       
    #    generate an arraay

        # nums = list(range(1, 10))
        # random.shuffle(nums)
        # dedupList = list(set(nums))
        # # np.save('myarray.txt', nums)
        # np.savetxt('test1.txt', nums, fmt='%d')

