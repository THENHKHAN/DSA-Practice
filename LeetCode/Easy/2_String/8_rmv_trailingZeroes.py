# 2710. Remove Trailing Zeros From a String :  https://leetcode.com/problems/remove-trailing-zeros-from-a-string/
'''
Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.
'''

def removeTrailingZeros(num: str) -> str:
        # return num.rstrip('0') # Runtime: 31 ms, faster than 97.17% of Python3 online submissions for Remove Trailing Zeros From a String.
        i = len(num) -1
        print(i)
        while ( num[i] >= '0'):
                if num[i] != '0':
                        return  num[0:i+1] ##Runtime: 39 ms, faster than 82.35% of Python3 online submissions for Remove Trailing Zeros From a String.
                print(i) 
                i -= 1      
                




strOfNum = "123400"
result = removeTrailingZeros(strOfNum)
print(f"Here is the string of number after removing trailling zeroes : {result}")