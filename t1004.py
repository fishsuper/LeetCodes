# 最大连续1的个数III

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n==0:
            return 0
        maxLen = 0
        left = 0
        curturn = 0
        curLen = 0
        for right in range(n):
            #while k==0 and left<=right-1 and nums[left]==0:
            #    left+=1
            #    curLen-=1
            if nums[right]==0:   # 特别注意后面两个if的顺序
                if  curturn>=k:
                    while nums[left]==1:
                        left+=1
                        curLen-=1
                    left+=1
                    #curturn-=1
                    curLen-=1
                if curturn<k:
                    curturn+=1
            curLen+=1
            maxLen = max(maxLen,curLen)
        return maxLen

# 用else
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n==0:
            return 0
        maxLen = 0
        left = 0
        curturn = 0
        curLen = 0
        for right in range(n):
            #while k==0 and left<=right-1 and nums[left]==0:
            #    left+=1
            #    curLen-=1
            if nums[right]==0: 
                if curturn<k:
                    curturn+=1
                else:
                    while nums[left]==1:
                        left+=1
                        curLen-=1
                    left+=1
                    #curturn-=1
                    curLen-=1
            curLen+=1
            maxLen = max(maxLen,curLen)
        return maxLen
        