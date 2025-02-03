# Output: "ABC"

from math import gcd


str1 = "ABCABd"
str2 = "ABC"

n1 = len(str1)
n2 = len(str2)

if str1+str2 != str2+str1:
    print("none")
else:
    print(str1[0:gcd(n1,n2)]) # gcd is a math function that shows the greatest common divisior