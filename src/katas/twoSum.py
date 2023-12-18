from typing import List
class TwoSum:
    # def twoSum(self, nums, target):
    #     dic = {}

    #     #A number can appear twice inside the same index, so I use a list
    #     for i in xrange(0, len(nums)):
    #         try:
    #             dic[nums[i]].append(i)
    #         except:
    #             dic[nums[i]] = []
    #             dic[nums[i]].append(i)

    #     try:
    #         for items_1 in dic[nums[i]]:
    #             for items_2 in dic[target-nums[i]]:
    #                 if(items_1+1 != items_2+1):
    #                     l = []
    #                     if(items_2+1 > items_1+1):
    #                         l.append(items_1+1)
    #                         l.append(items_2+1)
    #                     else:
    #                         l.append(items_2+1)
    #                         l.append(items_1+1)
    #                     return l
    #     except:
    #         pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[[nums.index(val),nums[ind +1:].index(target-val)+ ind +1] for ind,val in enumerate(nums) if target -val in nums[ind +1:]]
        return res[0]