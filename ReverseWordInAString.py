#Output: "blue is sky the"

s = "the sky is blue"

words = s.split()
res = reversed(words)
print(" ".join(res))  # Output: "blue is sky the"