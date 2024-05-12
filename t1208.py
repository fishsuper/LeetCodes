# 尽可能使字符串相等
# 滑动窗口

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if not s: return 0
        n = len(s)
        left = 0
        cost = 0
        curLen = 0
        maxLen = 0
        for right in range(n):
            cost = cost+abs(ord(s[right])-ord(t[right]))
            curLen += 1
            while cost>maxCost:
                left+=1
                cost = cost-abs(ord(s[left-1])-ord(t[left-1]))
                curLen -= 1
            maxLen = max(maxLen,curLen)
        return maxLen
