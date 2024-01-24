# Max Consecutive Ones- array 
# https://leetcode.com/problems/max-consecutive-ones/
# https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
        max = 0 # for storing the maximum 1s
        count= 0 # keepingtrack for 1
        for ele in nums :
            if ele == 1 :
                count += 1 
                if count > max :
                    max = count
            else:
                count  = 0 # after assigning the prevous consecutive count of one to max and move to the next consecutive 1s count.
        return max
# Runtime: 259 ms, faster than 92.45% of Python3 online submissions for Max Consecutive Ones. 




nums = [1,1,0,1,1,1]
print(f" the maximum number of consecutive 1's in the array : {findMaxConsecutiveOnes(nums)}")

'''
Intuition :
we have to find the maxumum count of 1s. and we dont have to care about other element.
so i focused on 1 only sarted counting as count then i noticed when i was trying on paper thtat i have to keep record of prevous count of 1 as well and allso need to check whether the prevous consecutive count of 1 was greater or less than than the current count. SO that's why i used one more conditon for finding max count
and if we move to theother than 1 element then stored the prevous count of 1 to a new varibale max and make the count as 0 so that we can count next consecutive 1.
DRAW or Practive WITH PEN PAPER

'''
# my post on LC:
# https://leetcode.com/problems/max-consecutive-ones/discuss/4616550/Max-Consecutive-Ones-in-T.C%3AO(n)-and-S.C%3AO(1)