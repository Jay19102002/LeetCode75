# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]
import collections
# queue = collections.deque()

# def ping(t):
#     if t is None:
#         return 1
#     queue.append(t)
#     while queue[0] < t - 3000:
#         queue.popleft()
#     return len(queue)
# Your code is mostly correct, but there are a few issues that need to be addressed.
# 1. The `ping` function should return `null` when the input is `null`. You
# 2. The `ping` function should return the correct count of elements in the queue. You
# 3. The `ping` function should handle the case when the input is `null` correctly.
# Here is the corrected code:
# python
class RecentCounter:
    def __init__(self):
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        if t is None:
            return None
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

t = [[], [1], [100], [3001], [3002]]
obj = RecentCounter()
print(obj.ping(t))  # Output: null


