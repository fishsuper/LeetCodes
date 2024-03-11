# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

def twoSum(nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    s = [i,j]
                    break
            if nums[i]+nums[j]==target:
                break
        return s


nums = [2,7,11,15]

## 使用哈希表
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []
