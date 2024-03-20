# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。 

# 我的解法
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0 = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==0: count0 += 1
        for j in range(count0):
            nums.remove(0)
            nums.append(0)
        return nums
        
# 官方解法，双指针，我按理解写的代码，需要找出第一个非零元位置
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                break
        left = i
        right = left+1
        while right<n:
            if nums[right]!=0:
                nums[left] = nums[right]
                nums[right] = 0
                left += 1
                right += 1
            else:
                right += 1
        return nums

# 双指针，官方代码
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        left = right = 0  #左右指针都从0开始，左指针只有在右指针的值非零才和右指针一起右移
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]  # 交换值的简洁写法
                left += 1
            right += 1

