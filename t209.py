# 滑动窗口

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if sum(nums)<target:
            return 0
        minLen = n
        if n==0:
            return 0
        left = 0
        cursum = 0
        for right in range(n):
            cursum = cursum+nums[right]
            while cursum>=target:
                minLen = min(minLen,right-left+1)
                left+=1
                cursum = cursum-nums[left-1]
            if minLen==1 and n!=1:
                break
        return minLen
