# 返回数组的多数元素、

# 哈希表
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        eleDict = dict()
        eleSet = set()
        majorNums = 0
        for i,num in enumerate(nums):
            if not num in eleSet:
                eleSet.add(num)
                eleDict[num] = 1
            else:
                eleDict[num]=eleDict[num]+1
            if eleDict[num]>n//2:
                majorNums = num
        return majorNums
        
### 以下官方解答
import collections
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 排序，中间元素必定是众数（巧妙）
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

# 随机化（很大概率会选中众数）
import random
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate

# 分治法：将数组分成两部分，众数必定仍是某一部分数组的众数
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)


# 投票算法
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
