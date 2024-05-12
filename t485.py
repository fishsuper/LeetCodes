# 数组中最大连续1的个数
# 我的解答，更快
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        n = len(nums)
        maxLen = 0
        while True:
            while left<n and nums[left]==0:
                left+=1
            right = left
            while right<n and nums[right]==1:
                right+=1
            maxLen = max(maxLen,right-left)
            left = right
            if left==n or right==n:
                break
        return maxLen

# 活用enumerate()遍历数组
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 0
        
        maxCount = max(maxCount, count)
        return maxCount
