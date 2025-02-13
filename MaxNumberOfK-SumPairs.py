# example
nums = [1,2,3,4]
k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

i = 0
j = len(nums)-1
output = 0
nums.sort()
while i < j:
    if nums[i] + nums[j] == k:
        output += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] < k:
        i += 1
    else:
        j -= 1

print(output)
    
            
