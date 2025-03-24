# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

from collections import defaultdict
import math
from typing import List

def calcEquation(equations,values,queries):
    graph = defaultdict(dict)
    memo = {}
    
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1/val
        
    def dfs(node, target, visited):
        if node not in graph or target not in graph:
            return -1.0
        if node == target:
            return 1.0
        if (node, target) in memo:
            return memo[(node, target)]
        
        visited.add(node)
        
        for neighbor, val in graph[node].items():
            if neighbor not in visited:
                result = dfs(neighbor, target, visited)
                if result != -1.0:
                    final_value = val * result
                    if math.isclose(final_value, -1.0, rel_tol=1e-9):
                        final_value = -1.0
                    memo[(node, target)] = final_value
                    return final_value   
        return -1.0
        
    return [dfs(c,d,set()) for c,d in queries]
            
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations,values,queries)) 
                                                                