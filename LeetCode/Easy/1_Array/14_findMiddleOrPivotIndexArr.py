# https://leetcode.com/problems/find-the-middle-index-in-array/
'''
Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

 

Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.
'''
from typing import List

def findMiddleIndex(nums: List[int]) -> int: # draw on COPYyou'll understand better
            # we'll approach by calculating total sum and then cumulative sum
        total_sum = sum(nums)
        cs = 0 
        for i in range(len(nums)):
                # cs = cumulative sum will be from left to current index element sum
                cs += nums[i]
                ls = cs - nums[i] # cumulative minus the current element we'll get the left sum. But try to think 1st calculating right IN THINKING or INITIALLY approaching.
                rs = total_sum - cs 
                print(f"cumulative : {cs}")
                print(f"leftSum : {ls}   ,  rightSum : {rs}")
                if ls == rs :
                        return i 
                
        return -1



nums = [2,3,-1,8,4] 
# nums = [1,-1,4]
# nums = [2,5]
print(f"Original Array : {nums}")
print(f" The middle index is :  {findMiddleIndex(nums)}") # 3
# Runtime: 40 ms, faster than 84.78% of Python3 online submissions for Find the Middle Index in Array.




#  Brute force : sum() with slicing - T.C= O(n^2) and S.C = O(1)
'''
# class Solution:
#     def findMiddleIndex(self, nums: List[int]) -> int:
# #         lets try using Brute force :
#           for i in range(len(nums)):
#             ls = sum( nums[ :i] ) # cal lef sum
#             rs = sum ( nums[i+1: ] ) # calc right from current index
#             if ls == rs :
#                 return i
#           return -1

'''
# Runtime: 44 ms, faster than 65.70% of Python3 online submissions for Find the Middle Index in Array.