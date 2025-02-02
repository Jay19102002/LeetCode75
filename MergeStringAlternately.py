# Example: Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s 

word1 = "ab"
word2 = "pqrs"
merged = []
i = j = 0

while i < len(word1) and j < len(word2):
    merged.append(word1[i])
    merged.append(word2[j])
    i +=1
    j +=1

merged.append(word2[i:])       
merged.append(word1[j:])       

print("".join(merged))