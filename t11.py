# 考虑到了如果对左端从0到右遍历，左端往右遍历只需考虑比左边都高的项，右端往左遍历时只需考虑比右边都高的项，
# 53/62个实例，超出时间限制

class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        n = len(height)
        for left in range(n-1):
            if height[left]<max(height[:left+1]):
                continue
            right = n-1
            while left<right:
                if height[right]<max(height[right:]):
                    right -= 1
                    continue
                maxarea = max(maxarea, (right-left)*min(height[left], height[right]))
                right -= 1
        return maxarea

# 改用哈希表存储真正需要遍历的项，用空间换时间，仍然在第53个算例出现超时间限制
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        left_hashtable = dict()
        right_hashtable = dict()
        n = len(height)
        for i in range(n):
            if height[i]>=max(height[:i+1]):
                left_hashtable[i] = height[i]
            if height[i]>=max(height[i:]):
                right_hashtable[i] = height[i]
        for left in left_hashtable:
            for right in right_hashtable:
                if left>=right:
                    continue
                maxarea = max(maxarea, (right-left)*min(left_hashtable[left],  right_hashtable[right]))
        return maxarea

# 优化边界条件，<=判断改成<，仍然是53/62
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        n = len(height)
        left_hashtable = dict()
        right_hashtable = dict()
        left_hashtable[0] = height[0]
        right_hashtable[n-1] = height[n-1]

        for i in range(1,n-1):
            if height[i]>max(height[:i]):
                left_hashtable[i] = height[i]
            if height[i]>max(height[i+1:]):
                right_hashtable[i] = height[i]
        for left in left_hashtable:
            for right in right_hashtable:
                if left>=right:
                    continue
                maxarea = max(maxarea, (right-left)* \
                min(left_hashtable[left],  right_hashtable[right]))
            
        return maxarea

 
