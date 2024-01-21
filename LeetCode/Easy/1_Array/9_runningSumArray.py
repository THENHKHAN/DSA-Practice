# https://leetcode.com/problems/running-sum-of-1d-array/

'''EX:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''

from typing import List

def runningSum(nums: List[int]) -> List[int]:
        # x = 0 
        # for i in range(len(nums)):
        #     x += nums[i]
        #     nums [i] = x
        # return nums
    # ALSO 
     for i in range(1, len(nums)):
          nums[i] += nums [i-1] #  Runtime: 33 ms, faster than 97.60% of Python3 online submissions for Running Sum of 1d Array.
     return nums



nums = [1,2,3,4]
print(f"Original Array : {nums}")
runningSum(nums)
print(f"Running sum of above array is :  is:  {nums}") # Running sum of above array is :  is:  [1, 3, 6, 10]
'''
Time complexity: O(n)
Space Complexity:O(1)

'''
