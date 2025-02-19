# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

def findPivot(nums):

    left = 0
    right = sum(nums)

    for i in range(len(nums)):
        right -= nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1               # corner case


nums = [1,7,3,6,5,6]
print(findPivot(nums))  # Output: 3