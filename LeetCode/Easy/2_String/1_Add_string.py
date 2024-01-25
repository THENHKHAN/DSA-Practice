# https://leetcode.com/problems/add-strings/
'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "11", num2 = "123"
Output: "134"
'''

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


def addStrings(num1: str, num2: str) -> str: 
        # sum_str = int(num1) + int(num2) 
    # return str(sum_str)                CAN'T do like this read th question carefully they told dont convert directly otherise will get: # ERROR: ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 5000 digits; use sys.set_int_max_str_digits() to increase the limit
  
#so lets try other way : we have to iterate one for other digit by digit
# we can convert each individual charcter and that won't exceed anything so in think in that way
#   1st think how to extract digits from last then think for how will you manage the carry and then condtion when to stop. Take example without carry type then carry type on paper pen
# and if one num is bigger then while summing think of one of them end earlier then put 0 at those palce while summing

            i = len(num1)-1
            j = len(num2)-1
            carry = 0
            # result_str = ""
            result_str=[]

            while(i>=0 or j>=0 or carry > 0):
                    dig1 = num1[i] if i >= 0 else 0
                    dig2 = num2[j] if j >= 0 else 0
                    _sum = int(dig1) + int(dig2) + carry # uses _sum since sum can  conflict with the exsiting sum funciton
                    result_str.append(_sum % 10)  # storing digits in a list
                    carry = _sum // 10
                    i -= 1
                    j -= 1

            return ''.join(map(str, result_str[::-1]))
 # Runtime: 35 ms, faster than 93.38% of Python3 online submissions for Add Strings.               
 # above using [] and join is more effecient than conacatening : 
'''Avoid String Concatenation: Instead of using string concatenation (result_str += ...), consider using a list to accumulate the digits and join them into a string at the end. This can be more efficient, especially if you are dealing with a large number of digits.
'''               
                
                
#     below was my appraoch for   concatenation           
            #     result_str += str(_sum%10) # getting last digigit of sum
            #         carry = _sum//10 # geting carry from sum
            #         i -= 1
            #         j -= 1
            # return result_str[::-1]
        # accepted : Runtime: 46 ms, faster than 51.37% of Python3 online submissions for Add Strings.


num1 ="456"#"11" #"11"
num2 = "77"#"199"#"123"
print(f"NumSTring1 = {num1} and NumString2 = {num2}")
print(f"Sum of the above two string (contains only numbers ) : {addStrings(num1, num2)}")
# I/O:
'''
NumSTring1 = 11 and NumString2 = 123
Sum of the above two string (contains only numbers ) : 134
'''

# # accepted : Runtime: 46 ms, faster than 51.37% of Python3 online submissions for Add Strings.