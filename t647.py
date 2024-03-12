## 从表头开始枚举解法

def huiwen(s: str) -> bool:
    n = len(s)
    flag = True
    if s == '':
        flag = False
    for i in range(n//2):
        if s[i] != s[-i-1]:
            flag = False
    return flag

def countSubstrings(s: str) -> int:
    n = len(s)
    count = n
    for i in range(n-1):
        for j in range(i+2,n+1):
            if huiwen(s[i:j]):
                count += 1
    return count

##  中心拓展

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            j = 0
            while i-j>=0 and i+j<=n-1 and s[i-j]==s[i+j]:
                count += 1
                j += 1
            j = 0
            if i<n-1 and s[i]==s[i+1]:
                while i-j>=0 and i+1+j<=n-1 and s[i-j]==s[i+1+j]:
                    count += 1
                    j += 1
        return count

s = 'abc'
print(countSubstrings(s))
solu = Solution()
print(solu.countSubstrings(s))
