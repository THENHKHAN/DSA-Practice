# https://leetcode.com/problems/plus-one/

'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4]


Input: digits = [4,3,2,1]
Output: [4,3,2,2]

Input: digits = [9]
Output: [1,0]
'''

def plusOne(digits) :
    num = ''.join(map(str, digits)) # we had to typecast into str each number since join funciton only join list of strings and not list of integrer 
    num = int(num)+1
    r = []
    while (num > 0) :
        dig = num % 10 
        r.append(int(dig))
        num = num//10

    return r[::-1]




# digits =[1, 9] # [2, 0]
# digits = [9,9,9] # [1, 0, 0, 0]
digits = [1,2,3] # [1,2,4]

# print(f"Original  list : {digits}")
# result = plusOne(digits)
# print(f"Resultant  list : {result}")

'''
Time Complexity: O(n)
Space Complexity: O(log(num))
'''

# above is BRUTE FORCE   : Runtime: 41 ms, faster than 46.77% of Python3 online submissions for Plus One.

#  Lets try to not use Extra space : The idea is to 1st check if dig < 9 then incremetn the dig by one and if not then make it zero and now pointer wil shift left now again check the 1st conditon.
# and if satistfy then incr
'''
[1,3,5] = 1st case - 1st cnditon met

[1,2,9] = [1,3,0] # 2nd case - 2nd condtion met
[9,9,9] = [1,0,0,0] # in this case  for all 9's 2nd condition met and then after ending of loop we just need to appned a 1 at oth index 

'''
def plusOne(digits) :
    n = len(digits)-1 # last index
    while( n >=0 ) :
        if ( digits [n] < 9):
            digits[n] += 1
            return digits
        else:
            digits[n] = 0
            n -= 1
    else:
        digits.insert(0,1)
        return digits 

# digits =[1,3,5]
# digits =[1,2,9]
digits =[9,9,9]
print(f"Original  list : {digits}")
result = plusOne(digits)
print(f"Resultant  list : {result}")

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''