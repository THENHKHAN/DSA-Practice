# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

''''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters

'''

def strStr(haystack: str, needle: str) -> int:
      


      return -1
        # return haystack.index(needle)  : inbuilt method of string 
      #   return haystack.find(needle) # https://www.geeksforgeeks.org/difference-between-find-and-index-in-python/ 
# Runtime: 41 ms, faster than 31.12% of Python3 online submissions for Find the Index of the First Occurrence in a String. BUT not prefenrable for logic building

haystack = "sadbutsad"
needle = "sad"
print(f"{haystack.split('sad')}")
print(f"larger  String haystack: {haystack}")
print(f"smaller String needle: {needle}")
print(f"first index occurence of {needle}  : {strStr(haystack, needle)}")# Above roman to Integer : 1994