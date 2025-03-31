# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
# Explanation:
# - 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
# - 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
# - 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
# Thus, [4,0,3] is returned.

def successfulPairs(spells, potions, success):
    potions.sort()
    result = []
    
    for spell in spells:
        left, right = 0, len(potions) - 1
        while left <= right:
            mid = (left + right) // 2
            if spell * potions[mid] >= success:
                right = mid - 1
            else:
                left = mid + 1
        result.append(len(potions) - left)
    
    return result

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
print(successfulPairs(spells, potions, success))  