# 不同路径数
# 动态规划

# 我的程序调用了Numpy包
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy
        arr = numpy.zeros((m,n))
        for i in range(m):
            arr[i][0]=1
        for i in range(n):
            arr[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i-1][j]+arr[i][j-1]
        return int(arr[m-1][n-1])
        
# 官方代码

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                f[j] += f[j - 1]
        return f[n - 1]
# 组合数    
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
