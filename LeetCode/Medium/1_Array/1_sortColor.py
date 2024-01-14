class Solution:

    def sortColors(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
# we'll be used THREE pointers (intuition - since 3 categories is here.)
#  our approach should be 0 should be in the starting , 1 should be in middle and 2 must be at the end
        
        # definig our three pointers:
        Left_Index = 0 # this take care of 0
        End_Index = len(nums)-1 # # this take care of 2
        Middle_Index = 0 # this take care of 1 - in this we dont have to replace or swap anything. It has be untouch
        # Middle_Index this will use for traversal
        
        while (Middle_Index <= End_Index):
                ele = nums[Middle_Index] 
                
                if (ele == 2 ): # then swap with the element which is at the end pointer and at the middle pointer and end pointer shift by 1 left 
                    
                    # swap(ele, nums[End_Index])
                    nums[Middle_Index] , nums[End_Index] = nums[End_Index], nums[Middle_Index]
                    End_Index -= 1

                elif (ele == 1 ): # move only middle and leave as it is left and end
                    Middle_Index += 1

                else:  # if element = 0 - move left and middle by 1
                    # swap(Middle_Index, Left_Index)
                    nums[Middle_Index], nums[Left_Index] = nums[Left_Index], nums[Middle_Index]
                    Middle_Index += 1
                    Left_Index   += 1
obj = Solution()
nums = [2,0,2,1,1,0]
obj.sortColors(nums)
print(nums)
            
                        
            
            
        