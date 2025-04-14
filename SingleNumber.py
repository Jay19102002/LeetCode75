# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4,1,2,1,2]
print(singleNumber(nums))  
    