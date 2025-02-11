# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [2,1]

left = 0
right = 0
# Traverse the array from left to right
while right < len(nums):
    # If the current element is not zero, swap it with the element at the left pointer
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        # Move the left pointer to the right
        left += 1
        # Move the right pointer to the right
    right += 1
    
    

print(nums)  
