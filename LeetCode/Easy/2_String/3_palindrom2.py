# 680. Valid Palindrome II 
# https://leetcode.com/problems/valid-palindrome-ii/
'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Explanation: we can remove b then we left with aa and that will palindrome

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters. means no need to use lower method

'''

def validPalindrome1(s: str) -> bool:
      # if not s.isalnum(): SINCE IN in Constraints they have mentioned taht in string there will be lowercase English letters.
      #   return True
#         deleting at most one. i have to take advantage. i will try to run loop and count if count>1 then false sinceone max can invalid
      l = 0
      r = len(s)-1
      countLeftMisMatch = 0
      countRightMisMatch = 0
      while (l<=r):
           if s[l] != s[r]:
                countLeftMisMatch += 1 # "deeee"
                l += 1
           else:
                l +=1
                r -=1
    #   for right mismatch
      l = 0
      r = len(s)-1
      while (l<=r):
           if s[l] != s[r]:
                countRightMisMatch += 1 # "eeeed"
                r -= 1
           else:
                l +=1
                r -=1
      print(countLeftMisMatch)
      print(countRightMisMatch)

      if countLeftMisMatch > 1 and countRightMisMatch > 1 :
           print("FASLSSSS")
           return False
      
      return True
# Runtime: 246 ms, faster than 6.90% of Python3 online submissions for Valid Palindrome II. O(N) but we are runing two loop 
# lets try in One loop

def  helper(s, l , r) : # will check palindrome after skippong one charater and return andthis return will be final return
     while (l <= r):
          if s[l] == s[r]:
               l +=1
               r -=1
          else :
            return False
     return True
     
def validPalindrome2(s: str) -> bool:
     l = 0
     r = len(s)-1
     while (l <= r):
          if s[l] == s[r]:
               l +=1
               r -=1
          else :
            # to skip left
           return helper(s, l+1, r) or helper(s, l, r-1) # this line of while loop . this line will take O(N) while=O(N) and helper fun will O(n) ==> O(n) 
     return True
#  Runtime: 110 ms, faster than 53.49% of Python3 online submissions for Valid Palindrome II.

# this will take TC= O(n)and SC= O(n)
def validPalindrome3(s: str) -> bool:
             l = 0
             r = len(s)-1
             while (l <= r ):
                if s[l] != s[r]:
                    skip_left, skip_right = s[l+1 :r+1] , s[l:r] # skipping either left pointer charcter or at right pinter character.
                    if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                        return True
                    else:
                        return False
                l +=1
                r -=1
             return True
        
# Runtime: 79 ms, faster than 86.18% of Python3 online submissions for Valid Palindrome II.
# But it took another space TC= O(N) , SC = O(N) still faster than the below two


# s = "aba" 
# s = "abca"
# s = "abc"
# s = "eeed"
s = "deee"
# s = "aydmda"
# s = "abc" # left misMatch , or if eeeed right mismatch
# if validPalindrome1(s) :
#     print("YES")
# else:
#     print("NO")
# if validPalindrome2(s) :
#     print("YES")
# else:
#     print("NO")
if validPalindrome3(s) :
    print("YES")
else:
    print("NO")