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
