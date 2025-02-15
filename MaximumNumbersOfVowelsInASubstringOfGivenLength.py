# sliding window example
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

def VowelSub(s,k):
    vowels = set('aeiou')
    count = 0
    maxx = count

    if len(s) < k: return 0                              # corner case
    
    for i in s[:k] :
        count += i in vowels                        #if i in vowels:                            
                                                     #   count += 1
    maxx = max(maxx,count)

    for i in range(k,len(s)):
        count += s[i] in vowels                     # if s[i] in vowels:                          
                                                    #     count += 1

        count -= s[i-k] in vowels                   # if s[i-k] in vowels:
                                                    #     count -= 1
        maxx = max(maxx,count)
        
    return maxx


s = "a"
k = 1
print(VowelSub(s,k))