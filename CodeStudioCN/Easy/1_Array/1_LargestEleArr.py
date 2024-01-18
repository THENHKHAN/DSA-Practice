from sys import *
from collections import *
from math import *
from typing import List

def largestElement(arr, n: int) -> int:

    # Write your code from here.
    maxEle = arr[0]
    for i in arr:
        if i > maxEle :
            maxEle = i

    return maxEle

def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]

num = [4, 7, 8, 6, 7, 6 ]
print(f"array: {num}")
print("The Largest element in the array is:", largestElement(num, 6))
print("*********** USing SORT method*********")
print("The Largest element in the array is:", sortArr(num))
