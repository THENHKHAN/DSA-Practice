
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        s = []
        for i in range(len(nums)):
            if nums[i] not in s :
                s.append(nums[i])
        j = 0
        l = len(s)
        for i in s :
            nums[j] = i
            j += 1
        
        return l # returning set length since unique
# above is  t : O(n) and S: O (n) Accepted :-->  Runtime: 78 ms, faster than 73.56% of Python3 online submissions for Remove Duplicates from Sorted Array.
# lets do it in a optimize way

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#          using TWO Pointer Approach : one will track the element from startto end and other is used to remove/avoid existing element or not 
          # i = 1  # this will move from start toend 
           rd = 0 # thus will bypass the duplicate
           for i in range(1, len(nums)):
                if nums[rd] != nums[i] :
                    rd += 1
                    nums[rd] = nums[i]
                    
                    
            
           return rd + 1
         
    '''
    https://www.youtube.com/watch?v=I0vmCnkcGW4
    https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/
    
    '''