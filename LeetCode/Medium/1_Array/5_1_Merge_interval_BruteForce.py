# https://leetcode.com/problems/merge-intervals/

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that 
cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

from typing import List


# about built-in sort method: In Python, the built-in sort() method uses a variant of Timsort, which is a hybrid sorting algorithm derived from merge sort and insertion sort.
# The time complexity of Timsort in the average and worst case is O(n log n), where n is the length of the list. This holds true for both 1D and 2D lists, as the sorting algorithm compares and swaps elements based on their values, not their internal structure.
# IMP 
'''
# Sorting a 2D list based on the first element of each sublist
list_2d = [[4, 2], [7, 1], [9, 3]]
list_2d.sort(key=lambda x: x[0])
'''
def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals) # size of the array

    # sort the given intervals:
    intervals.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = intervals[i][0], intervals[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            else:
                break
        ans.append([start, end])
    return ans



# intervals =[[1,3],[13,20], [2,6],[8,10],[15,18]]
intervals =[[1,3],[2,6],[8,10],[15,18]]
# intervals =[[1,4],[4,5]]
ans = merge(intervals)
print("The merged intervals are:")
for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
        print()


'''
My own approach 


def merge(intervals: List[List[int]]) -> List[List[int]]:
        # print(intervals)
        # 1st sort so that we can use logic that ith ele's 1st element must be greater than the (i-1)th . now we can visualize on line better. 
        intervals.sort() #it serve by default the above with lamda funcitonalilt i.e. based on 1st ele.  O(n log n), almost everywhere
        # print(intervals)
        storeArr = []
        count = 0
        for arrIndx in range(1,len(intervals)):
                # print(arrIndx) 
                end = intervals[arrIndx-1][-1] # 1st array ka last element
                # print(intervals[arrIndx])
                if end >= intervals[arrIndx][0]:# checking if 1st array last elemt greater than the next array's 1st ele then its mean overlapping
                       f_ele =  intervals[arrIndx-1][0] # 1st arr 1st elemtn 
                       sec_ele =  intervals[arrIndx][-1] # 2nd arr last elemtn 
                       storeArr.append([f_ele, sec_ele])
                else:# if last elemtn not eoverlapping then append it in the final arr.
                        storeArr.append(intervals[arrIndx])      
                # for i in range(len(arr)):                       
                #         
                #         nextArrPointer = i+1 # next array
                #         if end in 
                
        print(storeArr)
        return storeArr

# intervals =[[1,3],[13,20], [2,6],[8,10],[15,18]] - not worked my approach but below two is working goood 
intervals =[[1,3],[2,6],[8,10],[15,18]]
# intervals =[[1,4],[4,5]]
ans = merge(intervals)

'''