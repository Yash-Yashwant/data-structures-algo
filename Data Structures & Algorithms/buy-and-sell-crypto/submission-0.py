class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minValue=float('inf')
        currentValue=0
        maxProfit=0
        n = len(prices)

        for i in range(n):
            currentValue = prices[i]
            if currentValue < minValue:
                minValue=prices[i]
            if maxProfit < (currentValue - minValue):
                maxProfit = (currentValue - minValue)
        return maxProfit
            


        