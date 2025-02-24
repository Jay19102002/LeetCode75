# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
# - The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
# - The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
# There are no more stars, so we return "lecoe".

def removeStars(s):
    stack = []
    for char in s:
        if char == '*':
            if stack:           # stack not empty
                stack.pop()
            else:
                stack.append('*')
        else:
            stack.append(char)
    return ''.join(stack)

s = "leet**cod*e"
print(removeStars(s))  