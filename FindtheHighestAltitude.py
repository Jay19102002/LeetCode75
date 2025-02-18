# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
gain = [-4,-3,-2,-1,4,3,2]

def highestAltitude(gain):
    sum = 0
    maxo = 0
    for i in gain:
        sum+=i
        maxo = max(maxo,sum);
    return maxo

print(highestAltitude(gain))    #output 0