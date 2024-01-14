class Solution:
    def search(self, nums: List[int], target: int) -> int:
            left_index = 0
            right_index = len(nums)-1
            
            while( left_index <= right_index ):
                
                middle_index = ( left_index + right_index)//2 # give index
                middle_number = nums[middle_index]
                
                if middle_number < target:
                        left_index = middle_index + 1
                        
                elif middle_number > target :
                    right_index = middle_index - 1
                    
                else:
                    return middle_index
            else:
                return -1