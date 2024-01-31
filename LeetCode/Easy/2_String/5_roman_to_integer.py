
# 13. Roman to Integer : https://leetcode.com/problems/roman-to-integer/

# V - I = IV
# (Roman numerals)

# 5 - 1 = 4
# numbers
# you can  refer oline converter and calculator
# https://www.calculatorsoup.com/calculators/conversions/roman-numeral-calculator.php
# Roman numerals are usually written largest to smallest from left to right.
# LOGIC: if ith greater than (i+1)th then add in result  , and if ith less than (i+1)th then substract.
def romanToInt(s: str) -> int:
            n = len(s)
            translations = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
             }
            result = 0
            for i in range(0, n):
                cur = translations[s[i]]
                if i < n - 1 and cur < translations[s[i + 1]]:
                    result -= cur
                else:
                    result += cur
            return result


# input_roman = "IV"
# input_roman = "III"
# input_roman = "LVIII"
input_roman ="MCMXCIV"
print(f"String input roman: {input_roman}")
print(f" Above roman to Integer : {romanToInt(input_roman)}")# Above roman to Integer : 1994
# for conecpt LOGIC: https://www.youtube.com/watch?v=3jdxYj3DD98
# https://leetcode.com/problems/roman-to-integer/discuss/264743/Clean-Python-beats-99.78.
# https://leetcode.com/problems/roman-to-integer/discuss/2428756/Python-oror-Easily-Understood-oror-Faster-than-98-oror-Less-than-76-oror-O(n)
# https://leetcode.com/problems/roman-to-integer/discuss/3421656/Hash-Table-Concept-Python3