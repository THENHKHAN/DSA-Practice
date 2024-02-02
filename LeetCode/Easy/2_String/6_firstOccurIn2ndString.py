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

1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters

'''

def strStr(haystack: str, needle: str) -> int:
      
      for i in range(0, (len(haystack)-len(needle)+1)): 
            if needle in haystack[i : len(needle)+i] :
                  return i
      return -1# Runtime: 43 ms, faster than 20.92% of Python3 online submissions for Find the Index of the First Occurrence in a String.
        # return haystack.index(needle)  : inbuilt method of string 
      #   return haystack.find(needle) # https://www.geeksforgeeks.org/difference-between-find-and-index-in-python/ 
# Runtime: 41 ms, faster than 31.12% of Python3 online submissions for Find the Index of the First Occurrence in a String. BUT not prefenrable for logic building

haystack = "sadbutsad"
needle = "sad"
print(f"larger  String haystack: {haystack}")
print(f"smaller String needle: {needle}")
print(f"first index occurence of {needle}  : {strStr(haystack, needle)}")
#  we'll do later with 
'''
The two most common O(n) string searching algorithms are:

Boyer Moore: https://en.wikipedia.org/wiki/Boyer–Moore_string-search_algorithm
KMP: https://en.wikipedia.org/wiki/Knuth–Morris–Pratt_algorithm
'''
# ref: top 3 most voted soltuion
'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/3249783/Java-or-Easy-or-With-Explanation
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/12956/C%2B%2B-Brute-Force-and-KMP
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/535326/JavaPython-KMP-Solution-O(m%2Bn)-Clean-code

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/665448/AC-simply-readable-Python-KMP-Rabin-Karp

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/3677775/one-line-code-using-python-(-TC%3A-O(N)-or-SC%3A-O(1))

https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/discuss/4183742/Easiest-Big-IQ-fast-solution-or-Beats-97-of-solutions
'''
