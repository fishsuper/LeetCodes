# 买卖股票的最佳时机II
# 解答链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/solutions/2774929/jian-dan-di-pan-duan-mai-ru-mai-chu-de-t-g06t/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
        hold = False
        if prices[0]<prices[1]:
            hold = not hold
            inprice = prices[0]
        profit = 0
        for i in range(1,n-1):
            if prices[i]>prices[i-1] and prices[i]>=prices[i+1]: # 卖出条件
                hold = not hold
                outprice = prices[i]
                profit = profit+outprice-inprice
            if prices[i]<=prices[i-1] and prices[i]<prices[i+1]:
                hold = not hold
                inprice = prices[i]
                #profit = profit+outprice-inprice
        if hold and prices[n-1]>=prices[n-2]:
            outprice = prices[n-1]
            profit = profit+outprice-inprice
        return profit


