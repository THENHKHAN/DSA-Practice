# https://leetcode.com/problems/pascals-triangle/       prob-118
'''
Given an integer numRows, return the first numRows of Pascal's triangle. OR We have to return/Generate Pascal triangle and return

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
'''
# all end index elements will be 1
# ith row means i+1 number of element since i starts from 0
# each number is the sum of the two numbers directly above it . click on link you will see the picture how Pascal triangle look like
'''
Input: N = 5
Output:
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1

'''

from typing import List

def generatePascalTriangle(numRows: int) -> List[List[int]]:
        finalNums=[]
        finalNums.append([1])
        for i in range(numRows-1):
            newRow=[1]
            for j in range(i):
                newRow.append(finalNums[i][j]+finalNums[i][j+1])
            newRow.append(1)
            finalNums.append(newRow)
        return finalNums


pascal = generatePascalTriangle(numRows = 5)
print(pascal) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
