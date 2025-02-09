# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

nums = [1,2,3,4,5]


first = float('inf')    # float(infinity) = stores float value of infinity
second = float('inf')

for i in nums:
    if i <= first:
        first = i
    elif i <= second:
        second = i
    else:
        print(True)
        
print(False)