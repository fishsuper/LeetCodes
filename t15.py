# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
# 同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

def threeSum(nums: list[int]) -> list[list[int]]:
        nums.sort()
        tripleNums = []
        n = len(nums)
        if n<3:
            return []
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]+nums[-2]+nums[-1]<0:
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            left=i+1
            right=n-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    tripleNums.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                while left>i+1 and left<right and nums[left]==nums[left-1]:
                    left += 1
                while right<n-1 and right>left and nums[right]==nums[right+1]:
                    right -= 1
                if nums[i]+nums[left]+nums[right]<0:
                    left += 1
                elif nums[i]+nums[left]+nums[right]>0:
                    right -= 1
        return tripleNums


nums = [1,2,-2,-1]
ans = threeSum(nums)

print(ans)

