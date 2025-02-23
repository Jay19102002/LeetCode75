# Example 1:

#     3   2   1
#     1   7   6
#     2   7   7

# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:- (Row 2, Column 1): [2,7,7]

from collections import defaultdict

def equalPairs(grid):
    count = 0
    row_count = defaultdict(int)

    for row in grid:
        row_count[tuple(row)] += 1

    for col in zip(*grid):
        count += row_count[tuple(col)]

    return count

            

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(equalPairs(grid))  #Output 3