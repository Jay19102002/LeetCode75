# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.


def combinationSum(k, n):
    # return list(_ for _ in combinations(range(1,10), k) if sum(_) == n)       one line solution
    
    def backtrack(start, path, target):
        if target < 0 or len(path) > k:
            return
        if len(path) == k and target == 0:
            res.append(path[:])
            return
        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, path, target - i)
            path.pop()
    res = []    
    backtrack(1, [], n)
    return res

k = 3
n = 9
print(combinationSum(k, n))