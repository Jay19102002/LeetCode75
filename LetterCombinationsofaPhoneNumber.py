# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):
    if not digits:
        return []
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
    
    def backtrack(idx, combination):
    
        if idx == len(digits):        
            output.append(combination)
            return
        
        for letter in phone[digits[idx]]:
            backtrack(idx + 1, combination + letter)
 
    output = []
    backtrack(0, "")
    return output

digits = "23"
print(letterCombinations(digits))  

        
        
        
        
        
        
        
        
        