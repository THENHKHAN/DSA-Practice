# class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:

#         storeUniqTripples = []
#         for i in range(len(nums)):
#             # for next elem get
#             for j in range(i+1, len(nums)):
#                 # for next to this ele.
#                   for k in range(j+1, len(nums)):
#                      if nums[i]+nums[j]+nums[k] == 0:
#                            # Convert the list to a tuple before adding to the set
#                           triplet = sorted([nums[i], nums[j], nums[k]]) # sorting bcz to avoid duplicate in the result
#                           if triplet not in storeUniqTripples :
#                                 storeUniqTripples.append(triplet)
                               
                          
#         return storeUniqTripples

'''
Time Complexity:

The function uses three nested loops, each iterating over the length of the input nums. In the worst case, each loop can run up to the length of the array, resulting in a time complexity of O(n^3).
Within the innermost loop, there are constant-time operations like addition, sorting, and list appending. While sorting has a time complexity of O(log n), in this context, its impact is less significant compared to the overall triple nested loop.
Therefore, the dominant factor is the triple nested loop, and the overall time complexity is O(n^3).
Space Complexity:

The function uses a list (storeUniqTripples) to store unique triplets. In the worst case, all possible unique triplets are stored.
The number of unique triplets is determined by the number of combinations of three elements from the input array, which is roughly O(n^3).
Therefore, the space complexity is also O(n^3).
In summary:

Time Complexity: O(n^3)
Space Complexity: O(n^3)
'''

#  that's why we'll go for more optimal: lets go with similar approach like 2SUM with TWO  POINTER. Here tartget will be extract one by one from a loop and then look for the other two number by summing we should get 0 so we'll add those tripplets in our result.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while(l<r):
                total = nums[i]+nums[l]+nums[r]

                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:

                    res.append([nums[i],nums[l],nums[r]])
                    
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res
    
    '''
    Below code haves some issue: most probbaly TLE or some code minor issue
    
    def threeSum(nums) :
     nums.sort() # [-4,-1,-1,0,1,2]
     l = 0
     h = len(nums)-1
     store_triplet = []
     for i in range(len(nums)-2):
                     
          # print(i)
          l = i+1
          h = len(nums)-1

          while(l < h ):

              sum = nums[i] + nums[l] + nums[h] 
              if sum == 0 and [nums[i], nums[l], nums[h]] not in store_triplet:
                    store_triplet.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1
              elif (sum < 0): # means non of the elemetnt will give give correct since soretd so we need to icr left pointer
                    l += 1
              else : # when sum > 0 since sorted so w have to move to left to get the lesser number
                    h -= 1 

     return store_triplet
    
    '''

        