# https://leetcode.com/problems/single-number/
'''
Find the number that appears once, and the other numbers twice

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
Input: nums = [4,1,2,1,2]
Output: 4
# multiple wyas
https://leetcode.com/problems/single-number/discuss/1771720/C%2B%2B-EASY-SOLUTIONS-(SORTING-XOR-MAPS-(OR-FREQUENCY-ARRAY))
intuition is btter:
https://leetcode.com/problems/single-number/discuss/1771771/Think-it-through-oror-Time%3A-O(n)-Space%3A-O(1)-oror-Python-Go-Explained
'''

from typing import List
# from collections import Counter
#def singleNumber(nums: List[int]) -> int:
# #         1st thought hashing : count freq and return key whose key's value is 1
#          # freq = dict(Counter(nums))
#          freq ={}
#          for i in nums: # if we dont want to use Counter class
#             freq[i] = freq.get(i,0)+1
            
#          for i in freq:
#             if freq[i] == 1 :
#                 return i
#         Runtime: 111 ms, faster than 80.99% of Python3 online submissions for Single Number.
'''
 time complexity is O(n + k). 
 space complexity is O(k) since we are using a dictionary to store the frequency of each unique element.
 you can achieve the same result with better space complexity (O(1)) and T.C: O(n) using the XOR operation
'''
# so lets try optiomal approach:
'''
Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2
OR:
A^A=0
A^B^A=B
(A^A^B) = (B^A^A) = (A^B^A) = B This shows that position doesn't matter.
Similarly , if we see , a^a^a......... (even times)=0 and a^a^a........(odd times)=a

Here all the numbers except the single number appear twice and so will form a pair. Now, if we perform XOR of all elements of the array, the XOR of each pair will result in 0 according to the XOR property 1. The result will be = 0 ^ (single number) = single number (according to property 2).

So, if we perform the XOR of all the numbers of the array elements, we will be left with a single number.

Approach:
We will just perform the XOR of all elements of the array using a loop and the final XOR will be the answer.

Assume the given array is: [4,1,2,1,2]
XOR of all elements = 4^1^2^1^2
      = 4 ^ (1^1) ^ (2^2)
      = 4 ^ 0 ^ 0 = 4^0 = 4
Hence, 4 is the single element in the array.
SO Zero XOR with ANy element will rsult as  thta element : ex: anyNum^0 or 0^anyNum ===>anyNum - anyNum coulbe be any number -ve,+ve or zero 
NOTE: we dont have to woorry about how pair of equal will come together just rmember if all element are in pair of two or even number and only number is single then that single lement will be resultant.

https://leetcode.com/problems/single-number/discuss/1771720/C%2B%2B-EASY-SOLUTIONS-(SORTING-XOR-MAPS-(OR-FREQUENCY-ARRAY))
it has NlogN approahc as well . read it when you got time
'''
def getSingleElement(nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result



arr = [4, 1, 2, 1, 2]
ans = getSingleElement(arr)
print("The single element is:", ans) # The single element is: 4
