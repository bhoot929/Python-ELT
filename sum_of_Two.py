'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.


Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num = {}
        l = len(nums)
        if l <= 1:
            return False
        else:
            for i in range(l):
                if nums[i]  in dict_num:
                    return [dict_num[nums[i]],i]
                else:
                    dict_num[target-nums[i]] = i
