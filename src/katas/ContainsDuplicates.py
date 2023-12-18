# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
from typing import List
import time

class Numbers:
    def containsDuplicateByBruteForce(self, nums: List[int]) -> bool:
        # nums = input("Enter the array:")
        start_time_nanosec = time.time_ns() 
        loopNbr=1
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                print("loop nbr:", loopNbr)
                loopNbr=loopNbr + 1
                if nums[i] == nums[j]:
                    return True     
        end_time_nanosec = time.time_ns() 
        print("total in ns:", end_time_nanosec-start_time_nanosec)
        return False
    
    def containsDuplicateBySort(self, nums: List[int]) -> bool:
        start_time_nanosec = time.time_ns() 
        loopNbr=1
        nums.sort()
        n = len(nums)
        for i in range(1, n):
                print("loop nbr:", loopNbr)
                loopNbr=loopNbr + 1
                if nums[i] == nums[i - 1]:
                    return True
        end_time_nanosec = time.time_ns() 
        print("total in ns:", end_time_nanosec-start_time_nanosec)
        return False
    
    def containsDuplicateByHashSet(self, nums: List[int]) -> bool:
       
        seen = set()
        start_time_nanosec = time.time_ns() 
        loopNbr=0
        for num in nums:
            loopNbr +=1
            print("loop nbr:", loopNbr)
            if num in seen:
                return True
            seen.add(num)
        end_time_nanosec = time.time_ns() 
        print("total in ns:", end_time_nanosec-start_time_nanosec)   
        return False
    
    def containsDuplicateByHashMap(self, nums: List[int]) -> bool:
        start_time_nanosec = time.time_ns() 
        loopNbr=0
        seen = {}
        for num in nums:
            loopNbr += 1
            print("loop nbr:", loopNbr)
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        end_time_nanosec = time.time_ns() 
        print("total in ns:", end_time_nanosec-start_time_nanosec)     
        return False
        


    # a 5 item array would loop how many times
    
# 1-4
#     2-5


# i=1
# j=2-5=4 times

# i=2
# j=3,5=3times

# 2
# 1


# n=5, loop =4+3+2+1=10  sigma(n-1)
# n=100, loop=99+98...1 
# n=1000 lopp =

# sigma N = N*(N+1)/2
# sigma 4= 4*5/2=10
# sigma 10000=9999*10000/2=
    