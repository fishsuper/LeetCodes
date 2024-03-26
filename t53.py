# 最大子数组和
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 子数组是数组中的一个连续部分。

# 我的解法是滑动窗口，右指针每次往右拓展一步子数组，左指针需通过判断（只指向正值）确定是否向右滑动以收缩子数组
# cur_subsum记录指针所夹住的子数组的和

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        lst = [i for i in nums if i>0] 
        if lst==[]:
            return max(nums)
        n = len(nums)
        left = 0
        cur_subsum = nums[0]
        max_subsum = cur_subsum
        for right in range(1,n):
            cur_subsum = cur_subsum + nums[right]
            if nums[right]>0:
                while left<right and cur_subsum-nums[right]<0:
                    left += 1
                    cur_subsum = cur_subsum-nums[left-1]
                max_subsum = max(max_subsum, cur_subsum)

        return max_subsum

# 官方解法，动态规划或分治
                

        
