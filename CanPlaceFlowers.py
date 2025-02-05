# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


flowerbed = [1,0,0,0,1]         # Output: True
n = 1     

if n==0:            # corner case
    print(True)

for i in range(len(flowerbed)):
    left = (i==0) or flowerbed[i-1] == 0                        # left hand side of flowerbed
    right = (i == len(flowerbed)-1) or flowerbed[i+1] == 0      # right hand side of flowerbed
        
    if left and right and flowerbed[i] == 0:
        flowerbed[i] = 1
        n-=1
        if n == 0:
            print(True)

print(False)


 
