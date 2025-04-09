# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

def uniquePaths(m, n):
    aboveRow = [1]*n
    for _ in range(m - 1):
        currentRow = [1] * n
        for i in range(1,n):
            currentRow[i] = currentRow[i-1] + aboveRow[i]
        aboveRow = currentRow
    return aboveRow[-1]

m = 3
n = 2
print(uniquePaths(m, n))  