# 238. Product of Array Except Self :  https://leetcode.com/problems/product-of-array-except-self/?envType=list&envId=p8pddrk1 : 
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


# lets go for more optimize - read the link you'll get more solutions
# https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview
# (Prefix & Suffix Products)
def productExceptSelfBetter(nums: List[int]) -> List[int]:
            n, ans, suffix_prod = len(nums), [1]*len(nums), 1
            for i in range(1,n):
                ans[i] = ans[i-1] * nums[i-1]
            for i in range(n-1,-1,-1):
                ans[i] *= suffix_prod
                suffix_prod *= nums[i]
            return ans
# Runtime: 153 ms, faster than 97.30% of Python3 online submissions for Product of Array Except Self.



nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
# nums = [0,0]
print(f"Array  : {nums}")
# print(f"Product of above array except itself : {productExceptSelfBrute(nums)}")
print(f"Product of above array except itself : {productExceptSelfBetter(nums)}")

# MOST upvoted :
'''
https://leetcode.com/problems/product-of-array-except-self/discuss/1342916/3-Minute-Read-Mimicking-an-Interview     Brute --> Optimal
https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
https://hackernoon.com/how-to-find-the-product-of-all-elements-in-an-array-except-self-blind-75-leetcode            visula logic

https://leetcode.com/problems/product-of-array-except-self/discuss/3186745/Best-C%2B%2B-3-Solution-oror-DP-oror-Space-optimization-oror-Brute-Force-greater-Optimize-oror-One-Stop-Solution.
https://leetcode.com/problems/product-of-array-except-self/discuss/2996710/O(N)-Single-For-Loop-Solution-in-Python-(Easy-to-Understand)
'''

# synatx:
'''
nums = [1,2,3,4]
ans = [1]*len(nums)
print(ans) # [1,1,1,1]
means ans list all the elemtn will be one and of the same size as nums array
'''
