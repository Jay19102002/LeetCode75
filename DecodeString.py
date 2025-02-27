# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

def decode(s):
    stack = []
    
    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            subString = ""
            while stack and stack[-1] != "[":
                subString = stack.pop() + subString
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(int(num) * subString)

    return "".join(stack)

s = "3[a]2[bc]"
print(decode(s)) 
