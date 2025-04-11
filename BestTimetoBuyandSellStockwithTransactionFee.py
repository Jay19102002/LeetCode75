# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

def maxProfit(prices, fee):
    buy = float('-inf')
    sell = 0
    
    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, buy + price - fee)
        
    return sell
        
prices = [1,3,2,8,4,9]
fee = 2
print(maxProfit(prices, fee)) 