# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

from collections import Counter     # count frequency of characters
def closestr(word1,word2):
    w1 = Counter(word1)
    w2 = Counter(word2)
    if sorted(w1.values()) == sorted(w2.values()) and set(w1.keys) == set(w2.keys()):
        return True
    else:
        return False
    
    
word1 = "abbzzca"
word2 = "babzzcz"
print(closestr(word1,word2))  