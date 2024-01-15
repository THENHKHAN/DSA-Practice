def sortedSquares( nums) :
        result = []
        l = 0
        h = len(nums)-1
        while ( l <= h) :
            
            if (nums[l]**2 > nums[h]**2):
                result.append(nums[l]**2)
                l += 1
            else:
                result.append(nums[h]**2)
                h -= 1
                   
        return result[::-1]

nums = [-4,-1,0,3,10]
print (f"Sqr of sorted array : {sortedSquares(nums)}")