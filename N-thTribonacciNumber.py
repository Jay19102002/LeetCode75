# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

def tribonacci(n):
    t = [0,1,1]
    if n < 3:
        return t[n]
    
    for i in range(3, n+1):
        t[0],t[1],t[2] = t[1],t[2],sum(t)
        
    return t[2]

# Test the function with an example input
n = 25
print(tribonacci(n))  