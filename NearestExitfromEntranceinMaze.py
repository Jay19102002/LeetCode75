# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
from collections import deque

def nearestExit( maze, entrance):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    rows,cols = len(maze),len(maze[0])
    queue = deque([(entrance[0], entrance[1], 0)])
    maze[entrance[0]][entrance[1]] = '+'
    
    while queue:
        x,y,dist = queue.popleft()
        for dx,dy in directions:
            new_x,new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == '.':
                if new_x == 0 or new_x == rows-1 or new_y == 0 or new_y == cols-1:
                    return dist + 1
                maze[new_x][new_y] = '+'
                queue.append((new_x,new_y,dist+1))
    return -1
    
# Time complexity: O(m*n)
# Space complexity: O(m*n)

maze = [[".","+"]]
entrance = [0,0]
print(nearestExit(maze, entrance)) 