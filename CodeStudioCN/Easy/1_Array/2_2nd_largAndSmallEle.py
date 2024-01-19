# https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960
'''
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.
'''
from sys import *
from collections import *
from math import *
from typing import List

def getSecondLargestAndSmallestElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    maxEle = max(a)
    minEle = min(a)
    secLargEle = min(a)
    secSmallEle = max(a)
    for indx in range(len(a)):
        if a[indx] > secLargEle and a[indx] != maxEle:
            secLargEle = a[indx]
        if a[indx] < secSmallEle and a[indx] != minEle:
            secSmallEle = a[indx]
    return [secLargEle, secSmallEle]

num = [1, 2, 3, 4, 5]
# num = [3, 4, 5, 2]
print(f"array: {num}")
print("The Largest element in the array is:", getSecondLargestAndSmallestElements(6, num))
'''
array: [1, 2, 3, 4, 5]
The Largest element in the array is: [4, 2]
'''