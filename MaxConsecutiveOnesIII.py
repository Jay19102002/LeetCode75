# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2


def cosecutiveOnes(nums,k):
    zeroCount = 0
    maxx = zeroCount
    i = j = 0
    while j < len(nums):
        if nums[j] == 0:
            zeroCount += 1
        while zeroCount > k and nums[j] == 0:
            if nums[i] == 0:
                zeroCount -= 1
            i +=1
        maxx = max(maxx, j - i + 1)
        j += 1
    return maxx
    
print(cosecutiveOnes(nums,k))
