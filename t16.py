# 最接近的三数之和

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        three_sum = sum(nums[0:3])
        if n==3:
            return three_sum
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                if abs(target-three_sum)>abs(target-(nums[i]+nums[left]+nums[right])):
                    three_sum=nums[i]+nums[left]+nums[right]
                if (nums[i]+nums[left]+nums[right])==target:
                    return target
                if (nums[i]+nums[left]+nums[right])<target:
                    left += 1
                if (nums[i]+nums[left]+nums[right])>target:
                    right -= 1
        return three_sum

