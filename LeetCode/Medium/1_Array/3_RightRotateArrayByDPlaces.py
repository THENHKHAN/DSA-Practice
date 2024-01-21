# https://leetcode.com/problems/rotate-array/
'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''
from typing import List
def rotate_to_right(nums: List[int], k: int) -> None:
#         lets try T.c = O(i) and S.c = O(n) by slicing
    a = nums[0: len(nums)-k] # since right rotation
    print("1st : ", a)
    b = nums[len(nums)-k: ]
    print("2nd : ", b)
    nums[:] = [*b, *a]

# method-2
def reverseArray(nums, start , end ):
      while(start< end):
            nums[start], nums[end] = nums[end], nums[start]
            start +=1
            end -= 1
                        
def rotate_to_right2(nums, k ):
        # test cases covering
        if (len(nums) == 0):
            return;
        k = k % len(nums);
        if (k > len(nums)):
            return;
        if len(nums)<k:
            return
       
#         lets 1st rverse it so that i can make like left rotation
        reverseArray (nums, 0, len(nums)-1 )
        # print(f"reversed array1 : {nums}")
        # take 1st kth array  and reverse
        reverseArray(nums, 0, k-1)
        # print(f"reversed array2 : {nums}")
        reverseArray(nums, k, len(nums)-1)
        # print(f"reversed array3 : {nums}")


#       0 1 2 3 4 5 6
nums = [1,2,3,4,5,6,7] # [5, 6, 7, 1, 2, 3, 4] for k=3 to rigth rotation
k = 2
# print(f"Original Array : {nums}")
# rotate_to_right(nums, k) # not passing all cases. But still passing much cases
# print(f"List after left rotation by {k} Place/position :  {nums}")

'''
Time Complexity: O(1), slicing used.
Space Complexity: O(n) as new array created
'''
#       0 1 2 3 4 5 6
nums = [1,2,3,4,5,6,7] # [5, 6, 7, 1, 2, 3, 4] for k=3 to rigth rotation
# nums = [-1]
k = 3
print(f"Original Array : {nums}")
rotate_to_right2(nums, k) # not passing all cases. But still passing much cases
print(f"List after left rotation by {k} Place/position :  {nums}")

