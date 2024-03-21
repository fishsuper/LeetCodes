# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

# 循环遍历，暴力求解（其实也就是官方解答的滑动窗口）
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        m = len(p)
        n = len(s)
        if n<m:  # 考虑s的长度小于p的情形
            return []
        lp = list(p)
        lp.sort()
        left_index = []
        for i in range(n-m+1):
            substr = list(s[i:i+m])
            substr.sort()
            if substr==lp:
                left_index.append(i)
        return left_index

# 官方解答，优化的滑动窗口
    