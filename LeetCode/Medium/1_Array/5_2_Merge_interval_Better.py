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

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2 :
                return intervals
        intervals.sort() # NlogN
        result_interval = []
        result_interval.append(intervals[0]) # added 1st interval to avoid edge case
        for i in range(1, len(intervals)) : # ith interval array
               prv_intervalal_last_ele = result_interval[-1][1]  #result_interval[-1][1] prv interval's last element
               curr_intervalal_first_ele = intervals[i][0] # interval 1ts element 
        #       for non-overlapping case
               if curr_intervalal_first_ele > prv_intervalal_last_ele :
                       result_interval.append(intervals[i])
               else: # for overlapping case
                       result_interval[-1][1] =  max(result_interval[-1][1], intervals[i][1]) # maximum of current interval

        print(result_interval)
        print(intervals)

        return result_interval




intervals =[[1,3],[2,6],[8,10],[15,18]]
# intervals =[[1,4],[4,5]]
ans = merge(intervals)
print("The merged intervals are:")
for it in ans:
        print(f"[{it[0]}, {it[1]}]", end=" ")
        print()
# TC= NlogN