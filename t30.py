# 30. 串联所有单词的字串

# 每次都要copy列表words
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        m = len(s)
        unit_len = len(words[0])
        n = unit_len*len(words)
        indexs = []
        for i in range(m-n+2):
            left = i
            right = left+unit_len
            temp_words = words.copy()
            while s[left:right] in temp_words and right<=i+n:
                temp_words.remove(s[left:right])
                left += unit_len
                right += unit_len
            if temp_words==[]:
                indexs.append(i)
        return indexs

# 用Counter()对比两个列表是否相等
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        m = len(s)
        unit_len = len(words[0])
        n = unit_len*len(words)
        indexs = []
        for i in range(m-n+2):
            left = i
            right = left+unit_len
            sub_str = []
            while s[left:right] in words and right<=i+n:
                sub_str.append(s[left:right])
                left += unit_len
                right += unit_len
            if Counter(words)==Counter(sub_str):
                indexs.append(i)
        return indexs

