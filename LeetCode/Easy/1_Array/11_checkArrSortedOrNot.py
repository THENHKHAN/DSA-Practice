from typing import List


def check(nums: List[int])->bool:
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1] :
            return False        
    return True
    

nums = [1,2,3,4,5]
flag = check(nums)
if flag:
    print("True")
else:
    print("false") 

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[j] < arr[i]:
    #             return False

    # return True
'''
Time Complexity: O(N^2)
Space Complexity: O(1)
'''