def maxProfit(prices):
    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            total += prices[i]-prices[i-1]

    return total

print(maxProfit([7, 1, 5, 3, 6, 4])) # 7
print(maxProfit([1, 2, 3, 4, 5])) # 4
print(maxProfit([7, 6, 4, 3, 1])) # 0
print(maxProfit([6, 1, 3, 2, 4, 7])) # 7