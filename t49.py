# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

# 我的解法，遍历一遍字符串列表，将当前字符分裂成有序字符的元组，这样形成1个元组对多个字符串的映射，用字典（哈希表）存储这样的有限映射
# 如果当前的字符元组不在哈希表中，将其作为键、字符作为值加入哈希表
# 最后通过一次循环遍历哈希表的值，形成需要的输出列表
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashtable = dict()
        for str in strs:
            lst_str = list(str)
            lst_str.sort()
            if tuple(lst_str) not in hashtable:
                hashtable[tuple(lst_str)] = [str]
            else:
                hashtable[tuple(lst_str)].append(str)
        words = []
        for s in hashtable:
            words.append(hashtable[s])
        return words

strs = ["eat","tea","tan","ate","nat","bat"]
solu = Solution()
print(solu.groupAnagrams(strs))
