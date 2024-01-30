
# 14. Longest Common Prefix :https://leetcode.com/problems/longest-common-prefix/
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
from typing import List
def longestCommonPrefixBrute(strs: List[str]) -> str:
    sortedString = sorted(strs)
    # lets 1st handle if no common prefix found
    if strs[0][0] != strs[1][0] :# checking 1st string and 2nd string 1st character: Since "" return is only possible if all the string in the list initial charcter is different. SO if we check for one we can find the answer.
        return "bbbb"
    n = len(sortedString)
    str1 = sortedString[0]
    ans_str = ""
    
    for i in range(0, len(str1)):
        ch = str1[i] 
        match = True
        
        for j in range(1, n) :
            str2 = strs[j] 
            if  len(str2) < i or ch != str2[i]:# if we sort the list lexiographiclaly then (i-1)th the enever be grater than th ith if common prefix. Ex: ["ab", "a"]==> ["a", "ab"] i-> 0 and len(str2) =2. Thtat's why we sorted
                match = False
                break
        
        if match == False :
            break
        else:
            ans_str += ch
            print(ans_str)
    return ans_str

    # print(sortedString)

def longestCommonPrefixOptimal(strs: List[str]) -> str:
    ans_str = ""
    sorted_str = sorted(strs)
    # lets get 1st and last string  and compnare since sorted
    first = sorted_str[0]
    last = sorted_str[-1]
    min_str_len = min(first, last)
    for i in range (len(min_str_len)):
        if first[i] != last[i] :
           return ans_str
        ans_str += first[i]

    return ans_str
# Runtime: 42 ms, faster than 44.79% of Python3 online submissions for Longest Common Prefix.
         


# InputStr = ["dog","racecar","car"]
InputStr = ["flower","flow","flight"]
# InputStr = ["ab","a"]
print(f"List of String : {InputStr}")
print(f"Brute: Longest Common Prefix : {longestCommonPrefixBrute(InputStr)}")
print(f"Optimal: Longest Common Prefix : {longestCommonPrefixOptimal(InputStr)}")


# https://leetcode.com/problems/longest-common-prefix/discuss/3273176/Python3-oror-C%2B%2Boror-Java-19-ms-oror-Beats-99.91