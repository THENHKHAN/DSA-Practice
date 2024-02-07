# 238. Product of Array Except Self :  https://leetcode.com/problems/product-of-array-except-self/?envType=list&envId=p8pddrk1 : 
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
from typing import List

def productExceptSelfBrute(nums: List[int]) -> List[int]:
      result = []
      for i in range(len(nums)):
            prod = 1 
            for j in range(len(nums)):
                  if i == j : 
                        continue
                  else:
                        prod *= nums[j]
                        
            result.append(prod)
      return result
# the Time Complexity for this solutison would be O(n2).
'''
    Time Complexity : O(N^2), Where N is the size of the Array(nums). Here Two nested loop creates the time 
    complexity.

    Space complexity : O(1), Constant space. Extra space is only allocated for the Array(output), however the
    output does not count towards the space complexity.

    Solved using Array(Two Nested Loop). Brute Force Approach.

    Note : This will give TLE.

'''


# lets go for more optimize


nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
nums = [0,0]
print(f"Array  : {nums}")
print(f"Product of above array except itself : {productExceptSelfBrute(nums)}")

# MOST upvoted :
'''
https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview     Brute --> Optimal
https://hackernoon.com/how-to-find-the-product-of-all-elements-in-an-array-except-self-blind-75-leetcode            visula logic

https://leetcode.com/problems/product-of-array-except-self/discuss/3186745/Best-C%2B%2B-3-Solution-oror-DP-oror-Space-optimization-oror-Brute-Force-greater-Optimize-oror-One-Stop-Solution.
'''
