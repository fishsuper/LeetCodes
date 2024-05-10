# 爬台阶
# 递归
# 可以写出显示表达的递推公式，不需要隐式递归

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        numofUp = [1,2]
        for k in range(2,n):
            numofUp.append(numofUp[k-1]+numofUp[k-2])
        return numofUp[-1]
    
# y优化空间复杂度为O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        p=1
        q=2
        for k in range(2,n):
            p,q=q,p+q
        return q
    