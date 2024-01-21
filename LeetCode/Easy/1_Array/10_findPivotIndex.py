# https://leetcode.com/problems/find-pivot-index/

'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11


Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

'''
from typing import List

def pivotIndex(nums: List[int]) -> int:
    for i in range(len(nums)):
        left_sum = sum (nums[ :i])
        # print(f"left sum : {left_sum}")
        right_sum = sum (nums[i+1:])
        # print(f"left sum : {right_sum}")

        if left_sum == right_sum :
            return i
    return -1
    
# Optimize in O(n)
def pivotIndexOptimize(nums: List[int]) -> int:
        total_sum = sum(nums)
        cs = 0
        for i in range(len(nums)):
            cs += nums[i]# till current element
            left_sum = cs-nums[i]
            right_sum = total_sum-cs # working on current element
            if left_sum == right_sum :
                return i
        return -1



# nums = [1,7,3,6,5,6]
nums =[1,2,3]
print(f"Original Array : {nums}")
print(f"Pivote index is:  {pivotIndex(nums)}")
'''
This solution iterates through each index and calculates the sum of elements on its left and right sides. If the left sum is equal to the right sum, it means that the current index is the pivot index, 
and the function returns that index. If no pivot index is found, it returns -1.

Note: This brute-force approach has a time complexity of O(n^2)and Space O(n) due to the nested summation. There are more 
optimized solutions with O(n) time complexity, but the brute-force approach is a simple and straightforward way to understand the problem.
'''

'''
Time complexity: O(n^2)
Space Complexity:O(1)

'''


nums = [1,7,3,6,5,6]
# nums =[1,2,3]
print(f"Original Array : {nums}")
print(f"Pivote index Optimize is:  {pivotIndexOptimize(nums)}")

'''
Original Array : [1, 2, 3]
Pivote index is:  -1
Original Array : [1, 7, 3, 6, 5, 6]
Pivote index Optimize is:  3
'''