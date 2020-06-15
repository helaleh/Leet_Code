def maxProfit( prices):

        profit = 0
        a = len(prices)

        for i in range(1, a):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

input=[7,6,5,1,5,8]
print(maxProfit(input))
