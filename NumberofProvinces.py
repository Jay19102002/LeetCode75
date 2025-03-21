# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
import collections
def findCircleNum(isConnected):
    visited = set()
    count = 0
    def bfs(node):
        nonlocal count 
        count +=1
        qu = collections.deque()
        qu.append(node)
        while qu:
            temp = qu.popleft()
            visited.add(temp)
            for i in range(len(isConnected)):
                if i not in visited and isConnected[temp][i]:
                    qu.append(i)
        return
    for i in range(len(isConnected)):
        if i not in visited:
            bfs(i)
    return count

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(isConnected))  