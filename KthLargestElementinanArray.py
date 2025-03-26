# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

def findKthLargest( nums, k):
    return sorted(nums, reverse = True) [k-1]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))  # Output: 5