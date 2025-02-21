# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
def occurNo(arr):
    map = {}
    for i in arr:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    
    if len(set(map.values())) == len(map.values()):
        return True
    else:
        return False

    
arr = [1,2,2,1,1,3]
print(occurNo(arr))