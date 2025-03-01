# Input: senate = "RDD"
# Output: "Dire"
# Explanation: 
# The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
# And the second senator can't exercise any rights anymore since his right has been banned. 
# And the third senator comes from Dire and he can ban the first senator's right in round 1. 
# And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
import collections
def Dota2senate(senate):
    radiantq = collections.deque()
    direq = collections.deque()
    senate = list(senate)
    n = len(senate)
    for i, char in enumerate(senate):
        if char == 'R':
            radiantq.append(i)
        else:
            direq.append(i)

    while radiantq and direq:
        direqTurn = direq.popleft()
        radientqTurn = radiantq.popleft()
        if direqTurn < radientqTurn:
            direq.append(radientqTurn + n)
        else:
            radiantq.append(direqTurn + n)
    
    return "Radiant" if radiantq else "Dire"

senate = "RDD"
print(Dota2senate(senate)) 