# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
def subarray(nums):
    res = 0
    l = r = 0
    for i in nums:
        if i == 1:
            r += 1
        else:
            # When encountering a 0, update the result and reset l and r
            res = max(res, l + r)
            l = r  # Move the left window to the right of the current 0
            r = 0  # Reset the right window
        # Update the result in each iteration
        res = max(res, l + r)
    
    # Handle the case where the last element is 1
    res = max(res, l + r)
    
    # If the entire array is 1s, we need to delete one element
    if res == len(nums):
        return res - 1
    else:
        return res

# Test case
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(subarray(nums))  # Output: 5