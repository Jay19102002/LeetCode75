# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)

def flip(a, b, c):
    flips = 0
    while a > 0 or b > 0 or c > 0:
        bit_a = a & 1
        bit_b = b & 1
        bit_c = c & 1
        if bit_c == 0:
            flips += (bit_a + bit_b)  
        else:
            if bit_a == 0 and bit_b == 0:
                flips += 1  
        a >>= 1
        b >>= 1
        c >>= 1
    return flips

a = 2
b = 6
c = 5
print(flip(a, b, c))  