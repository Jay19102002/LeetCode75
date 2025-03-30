# Binary Search

# Input: n = 10, pick = 6
# Output: 6

def binary(n,pick):
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid == pick:
            return mid
        elif mid < pick:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 10
pick = 6
print(binary(n,pick)) 