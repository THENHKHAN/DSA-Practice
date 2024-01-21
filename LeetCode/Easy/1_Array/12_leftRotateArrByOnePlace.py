# https://takeuforward.org/data-structure/left-rotate-the-array-by-one/

'''
Left Rotate the Array by One
Problem Statement: Given an array of N integers, left rotate the array by one place.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation: 
Since all the elements in array will be shifted 
toward left by one so ‘2’ will now become the 
first index and and ‘1’ which was present at 
first index will be shifted at last.


Example 2:
Input: N = 1, array[] = {3}
Output: 3
Explanation: Here only element is present and so 
the element at first index will be shifted to 
last index which is also by the way the first index.
'''
from typing import List
def left_rotate_by_one_place(nums: List[int], d: int) :
     x = nums[0]
     j = 0
     for i in range(len(nums)-1):
          nums[i] = nums[i+1] # shifting all the elemtn toward left and at the end index we placed 1st index element.
          j +=1
     nums[j] = x

d = 1;
arr = [1, 2, 3, 4, 5] #  [2, 3, 4, 5, 1]
print(f"Original Array : {arr}")
left_rotate_by_one_place(arr, d)
print(f"List after left rotation by One Place :  {arr}")

'''
Time Complexity: O(n), as we iterate through the array only once.

Space Complexity: O(1) as no extra space is used
'''