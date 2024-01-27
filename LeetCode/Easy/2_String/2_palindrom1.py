#125. Valid Palindrome :  https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
#         lets use two pointer approach one would be at last index and one at the start index
        start = 0
        end= len(s)-1
        while (start<end):
        #    print(f"l {start}: {s[start]}  r{end}:{s[end]}")
           if not s[start].isalnum(): # since it can contain , or # or      space so that we can ignore andm move formaward
                start +=1 
           elif not s[end].isalnum():
                 end -= 1
               
           elif s[start].lower() == s[end].lower() : # marhcing character by character
              start +=1 
              end -= 1
           
           else:
                return False
        return True

s = "A man, a plan, a canal: Panama"
if isPalindrome(s) :
    print("YES")
else:
    print("NO")