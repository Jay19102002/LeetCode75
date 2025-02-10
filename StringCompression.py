# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

chars = ["a","a","b","b","c","c","c"]

n = len(chars)
if n < 2:
    print(n)

i = j = 0
while i < n:
    count = 1
    while i < n-1 and chars[i]==chars[i+1]:
        i+=1
        count+=1

    chars[j] == chars[i]
    j+=1

    if count > 1:
        for val in str(count):
            chars[j] = val
            j+=1
    
    i += 1
print(j)

print(chars)
        

