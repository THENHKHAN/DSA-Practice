# https://takeuforward.org/data-structure/rotate-array-by-k-elements/

'''
Rotate array by K elements

Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

Example 2:
Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
Output: 9 10 11 3 7 8
Explanation: Array is rotated to right by 3 position.

'''
from typing import List
def left_rotate_by_Dth_place(nums: List[int], d: int) :
        a = nums[0:d] # oth to dth positiion -1 
        b = nums[d: ] # dth posiiton to last element 
        nums[ : ] = [*b, *a]

# method-2 
def reverseArray(lst, left, right) : # for reversing array
        while (left<right):
                lst[left], lst[right] = lst[right], lst[left]
                left += 1
                right -= 1
        
        
# Approach 2: Using ” Reversal Algorithm “ # ref: https://www.studytonight.com/python-programs/python-program-for-reversal-algorithm-for-array-rotation
def left_rotate_by_Dth_placeOptimal(nums: List[int], d: int) :
            # lets reverse 1st arr before dth indx : [1, 2, 3, 4, 5, 6, 7] ==> [3, 2, 1, 4, 5, 6, 7]
            reverseArray(nums,0, d-1 ) # # since we need to exlude the dth positon
            # lets reverse the other from dth to end : [3, 2, 1, 7, 6, 5, 4]
            reverseArray(nums, d, len(nums)-1) # d to last idex
            # now again we need to rverse # 
            reverseArray(nums, 0, len(nums)-1)
            # print(nums) #[4, 5, 6, 7, 1, 2, 3]

d = 2;
arr = [1, 2, 3, 4, 5] #  [4, 5, 1, 2, 3]
print(f"Original Array : {arr}")
left_rotate_by_Dth_place(arr, d)
print(f"List after left rotation by {d} Place/position :  {arr}")
'''
Time Complexity: O(1), slicing used.
Space Complexity: O(n) as new array created
'''
print("*************  Using ” Reversal Algorithm “    ******************")
     

nums = [1, 2, 3, 4, 5, 6, 7]
d = 3
print(f"Original Array : {nums}")
left_rotate_by_Dth_placeOptimal(nums, d)
print(f"List after left rotation by {d} Place/position :  {nums}")

'''
Original Array : [1, 2, 3, 4, 5]
List after left rotation by 2 Place/position :  [3, 4, 5, 1, 2]
*************  Using ” Reversal Algorithm “    ******************
Original Array : [1, 2, 3, 4, 5, 6, 7]
List after left rotation by 3 Place/position :  [4, 5, 6, 7, 1, 2, 3]
'''

'''
Time Complexity: O(n), Using ” Reversal Algorithm “.
Space Complexity: O(1) no extra space used
'''