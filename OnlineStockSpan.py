# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]

# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            val, count = self.stack.pop()
            res += count
        
        self.stack.append((price, res))
        return res

spanner = StockSpanner()
print(spanner.next(100)) # return 1
print(spanner.next(80))  # return 1
print(spanner.next(60))  # return 1
print(spanner.next(70))  # return 2
print(spanner.next(60))  # return 1
print(spanner.next(75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(spanner.next(85))  # return 6
