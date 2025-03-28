# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation: 
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.

from heapq import heappush, heappop

def maxScore(nums1, nums2, k):
    n = len(nums1)
    nums = sorted(zip(nums1, nums2), key=lambda x: -x[1])
    heap = []
    total = 0
    
    for i in range(k):
        total += nums[i][0]
        heappush(heap, -nums[i][0])
        
    ans = total * nums[k - 1][1]
    
    for i in range(k, n):
        total += nums[i][0]
        heappush(heap, -nums[i][0])
        total += -heappop(heap)
        ans = max(ans, total * nums[i][1])
        
    return ans

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
print(maxScore(nums1, nums2, k)) 
