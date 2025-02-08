# example:-
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

nums = [1,2,3,4]
n = len(nums)
ans = [1] * n       # [1,1,1,1]

for i in range(1,n):
    ans[i] = ans[i-1] * nums[i-1]   # left   ans = [1,1,2,6]

right = 1

for i in range(n - 1, -1, -1):      # right    
    ans[i] = ans[i] * right         # ans = [24,12,8,6]
    right = right * nums[i]         # right = 24*1=24

print(ans)

# time = O(n)
# space = O(1)