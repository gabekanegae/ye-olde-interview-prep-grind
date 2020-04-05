def maxProfit(prices):
    i, j = 0, 1

    total = 0
    while j < len(prices):
        while j < len(prices) and prices[j] > prices[j-1]:
            j += 1
        
        total += prices[j-1]-prices[i]

        i = j
        j = j+1

    return total

print(maxProfit([7, 1, 5, 3, 6, 4])) # 7
print(maxProfit([1, 2, 3, 4, 5])) # 4
print(maxProfit([7, 6, 4, 3, 1])) # 0