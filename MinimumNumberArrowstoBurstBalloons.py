# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

def findMinArrowShots(points):
    if not points:
        return 0

    # Sort the points based on their end times
    points.sort(key=lambda x: x[1])

    count = 1
    prev_end = points[0][1]

    for i in range(1, len(points)):
        if points[i][0] > prev_end:
            count += 1
            prev_end = points[i][1]

    return count

points = [[1,2],[3,4],[5,6],[7,8]]
print(findMinArrowShots(points)) 