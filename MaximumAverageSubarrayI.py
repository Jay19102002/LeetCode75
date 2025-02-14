# Input: 
nums = [1,12,-5,-6,50,3]
k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


# Initialize the sum of the first k elements
sum_k = sum(nums[:k])                                  # 0:3 != 4

# Initialize the maximum average
max_average = sum_k / k

# Iterate over the rest of the array
for i in range(k, len(nums)):

    # Update the sum by subtracting the first element of the previous window and adding the current element
    sum_k = sum_k - nums[i - k] + nums[i]

    # Return the maximum average
    max_average = max(max_average, sum_k / k)

print(max_average) 


