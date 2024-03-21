# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。

# 前n部分和（超出时间限制）
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        fnsum = []
        #for i in range(n):
        #    fnsum.append(sum(nums[:i+1]))
        for i in range(n):
            s = s+nums[i]
            fnsum.append(s)
        c = 0
        for i in range(n):
            c = c+fnsum.count(k)
            del fnsum[0]
            fnsum = [j-nums[i] for j in fnsum]
        return c

# 优化代码，计算fnsum变成计算k+nums[i]，可以通过全部实例
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        if k<min(nums):
            return 0
        n = len(nums)
        fnsum = []
        s = 0
        for i in range(n):
            s = s+nums[i]
            fnsum.append(s)
        c = 0
        for i in range(n):
            c = c+fnsum.count(k)
            del fnsum[0]
            k = k+nums[i]
        return c
