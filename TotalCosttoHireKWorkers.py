# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.

import heapq
def totalCost(costs, k, candidates):
    i = 0
    j = len(costs)-1        #reverse order
    pq1=[]
    pq2=[]
    ans = 0
    while k > 0:
        while len(pq1) < candidates and i <= j:
            heapq.heappush(pq1, costs[i])
            i += 1
            
        while len(pq2) < candidates and i <= j:
            heapq.heappush(pq2, costs[j])
            j -= 1
        
        t1 = pq1[0] if pq1 else float('inf')
        t2 = pq2[0] if pq2 else float('inf')
        
        if t1 <= t2:
            ans += t1
            heapq.heappop(pq1)
        else:
            ans += t2
            heapq.heappop(pq2)
        
        k -= 1
    return ans

costs = [17,12,10,2,7,2,11,20,8]
k = 3
candidates = 4
print(totalCost(costs, k, candidates))  # Output: 11