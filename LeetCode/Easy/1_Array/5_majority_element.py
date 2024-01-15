# ⌊x⌋ represents the floor function which rounds x down to the nearest integer. For example, ⌊3.8⌋ is 3, and ⌊-2.5⌋ is -3.Draw on line you'll understand better for more.
import math

def majorityElement(nums) :
    lst_length = len(nums)
    element_freq_count= {}
    for ele in nums :
        if ele in element_freq_count :
            element_freq_count[ele] = element_freq_count[ele] + 1
        else:
            element_freq_count[ele] = 1

    for key, value in element_freq_count.items():
        if element_freq_count[key] > math.floor(lst_length/2):
            return key

# nums = [2,2,1,1,1,2,2]
nums = [6,5,5]
print (f"Here is th majority elemtn : {majorityElement(nums)}") # Here is th majority elemtn : 5