# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Sort the intervals based on their end times
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1
        else:
            prev_end = intervals[i][1]

    return count

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverlapIntervals(intervals))  