# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

def collision(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:        # -num
                stack.pop()
            elif diff > 0:      # +num
                a = 0
            else:               # ==num
                a = 0
                stack.pop()
        if a:                   # edge case
            stack.append(a)        
    return stack


asteroids = [5,10,-5]
print(collision(asteroids))  