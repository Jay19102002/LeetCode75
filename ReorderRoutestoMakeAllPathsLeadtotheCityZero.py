#               3 <-- 2
#              /^
#            1^
#           /^
#         0^ <-- 4 <--> 5

# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

def minReorder(n, connections):
    seen = {0}
    # Counter for the number of roads that need to be reversed
    ans = 0
    
    while len(seen) < n:
        check = []
        for path in connections:
            if path[1] in seen:
                seen.add(path[0])
            elif path[0] in seen:
                seen.add(path[1])
                ans += 1
            else:
                check.append(path)
        # Reverse the order of unprocessed connections for the next iteration
        connections = check[::-1]
    
    return ans

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, connections)) 