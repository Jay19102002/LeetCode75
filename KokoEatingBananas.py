# Input: piles = [3,6,7,11], h = 8
# Output: 4

def eating(piles,h):
    left = 1
    right = max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid # ceil(pile / mid)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left

piles = [30,11,23,4,20]
h = 5
print(eating(piles,h))