#  给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
# 循环遍历，暴力求解
def notsame(s: str) -> bool:
    return len(s)==len(set(s))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_num = 0
        for i in range(n):
            j = i+2
            while j<=n and notsame(s[i:j]):
                j = j+1
            max_num = max(j-1-i, max_num)
        return max_num

ans = Solution()
s = "pwwkew"
print(ans.lengthOfLongestSubstring(s))

# 解法2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 1
        n = len(s)
        if n==1:
            return 1
        else:
            max_num = 0
            while n!=1 and right<n:
                if len(s[left:right])==len(set(s[left:right])):
                    max_num = max(max_num,right-left)
                    right += 1
                    if right==n and len(s[left:right])==len(set(s[left:right])):
                        max_num = max(max_num,right-left)
                else:
                    left += 1
        return max_num
        

## 滑动窗口（官方解答）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len

# 自己写的滑动窗口版本

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        max_length = 0
        left = 0
        for right in range(1,n+1):
            if len(set(s[left:right]))==right-left:
                max_length = max(max_length, right-left)
            while len(set(s[left:right]))!=right-left:
                left += 1
        return max_length
