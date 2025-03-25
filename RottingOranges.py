# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

from collections import deque

def orangesRotting(grid):
    rows = len(grid)
    if rows == 0:
        return -1
    
    cols = len(grid[0])
    fresh = 0
    rotten = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while rotten and fresh > 0:
        minutes += 1
        for _ in range(len(rotten)):
            x,y = rotten.popleft()
        
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                xx,yy = x + dx, y + dy
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue
                
                fresh -= 1
                grid[xx][yy] = 2
                rotten.append((xx,yy))
    
    return minutes if fresh == 0 else -1

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))  