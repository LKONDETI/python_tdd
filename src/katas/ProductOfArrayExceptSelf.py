# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.



from functools import reduce
import time

class ProductOfArray:
    def product_of_array_except_self(self, nums):
        start_time_nanosec = time.time_ns()
        prod, zero_cnt = reduce(lambda a, b: a*(b if b else 1), nums, 1), nums.count(0)
        if zero_cnt > 1: return [0]*len(nums)
        for i, c in enumerate(nums): # enumerate keeps track of the no of iterations
            if zero_cnt: nums[i] = 0 if c else prod
            else: nums[i] = prod // c
        end_time_nanosec = time.time_ns() 
        print("total in ns:", end_time_nanosec-start_time_nanosec)
        return nums
    
    def ProductOfArrayExcept(self,nums): 
        n = len(nums)
        answer = []

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            answer.append(product)

        return answer
        