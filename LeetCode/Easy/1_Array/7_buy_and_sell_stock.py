# 121. Best Time to Buy and Sell Stock
'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

# def maxProfit(self, prices: List[int]) -> int:
# # you must buy before you sell.
# def maxProfit( prices): # Brute Force Approach
#     mxProf = 0
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[j]-prices[i] > 0:
#                 mxProf = max(mxProf, prices[j]-prices[i])
    
#     return mxProf
        
arr = [7, 1, 5, 3, 6, 4]
# maxPro = maxProfit(arr)
# print("Max profit is: ", maxPro)
# Time Limit Exceeded

# lets try to in O(n) ************************************

def maxProfit( prices): 
    mxProf = 0
    minPrice  = prices[0] # trying to keep track of the minimum price in your minPrice variable, 

    for indx in range(len(prices) ):
        minPrice = min( prices[indx], minPrice)
        diff = prices[indx] - minPrice
        if diff > mxProf :
            mxProf = diff
    
    return mxProf



arr = [7, 1, 5, 3, 6, 4]
maxPro = maxProfit(arr)
print("Max profit is: ", maxPro)

'''
Time complexity: O(n)
Space Complexity: O(1)

'''





