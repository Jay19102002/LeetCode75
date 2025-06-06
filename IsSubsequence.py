# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

s = "abc"
t = ""

i = j = 0

while i<len(t) and j < len(s):
    if s[j] == t[i]:
        j += 1
    i += 1
if (j == len(s)):
    print(True)
else:
    print(False)