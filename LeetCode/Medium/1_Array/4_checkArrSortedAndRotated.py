
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/#:~:text=Input%3A%20nums%20%3D%20%5B2%2C,no%20rotation)%20to%20make%20nums.

'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
'''
from typing import List

# MOST IMP: DOnt think of roation 1st forst about how you will manage/check array is not not shorted in incre order
# count var is checking that . DRAW ON PAPER
                
def check(nums: List[int]) -> bool:
          count  = 0
          for i in range(1,len(nums)):
                 if nums[i-1] > nums[i] :
                        count += 1                        
                    
          if  nums[0] < nums[-1] :
                count += 1
          return count <= 1 # equal since number can be duplicate 
    
    
'''
            # 1st we need to check whether the input array is sorted or not if not sorted then retunr false here dont go further . but if sorted then go further step
         # for i in range(1, len(nums)):
         #    if nums[i] < nums[i-1] :
         #        return False        
        #return True #- hnalding edge case
'''
'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
# WE'LL LOOK LATER
# 1 - look for exactly one or zero(in case ratate 0 position) pair must exist where (i-1)th element must must be greater than ith elememt (if furteher someone rotate by any psotion)
# 2- also look 0th lement must be less than right most elemtn i.e. (-1)th element
#and count must be less than or equal to 1
'''
12345 ==> 34512 dont thins after rotating think before roating means athink about sorting checking
'''

nums = [1,2,3,4,5]
flag = check(nums)
if flag:
    print("True")
else:
    print("false") 