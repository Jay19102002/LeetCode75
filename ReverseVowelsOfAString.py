# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".


s = "IceCreAm"

s = list(s)
left = 0
right = len(s) - 1
vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']

print("original string: ")
print("".join(s))
while left < right:
    if s[left] not in vowels:
        left +=1
    elif s[right] not in vowels:
        right -= 1
    else:
        s[left],s[right] = s[right],s[left]    
        left +=1
        right -=1
print("After reverse: ")
print("".join(s))
