# 买卖股票的最佳时机
# 双指针

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        sin = 0
        sout = 0
        n = len(prices)
        for sout in range(1,n):
            if prices[sout]>prices[sin]:
                profit = max(profit,prices[sout]-prices[sin])
            else:
                sin = sout
        return profit
        
# 运算时间的小优化
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        sin = 0
        sout = 0
        n = len(prices)
        for sout in range(1,n):
            if prices[sout]>prices[sin]:
                if prices[sout]>prices[sout-1]: # 多加了一个条件
                    profit = max(profit,prices[sout]-prices[sin])
            else:
                sin = sout
        return profit
