# 不同路径II（障碍物）

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        import numpy
        ways = numpy.zeros((m,n))
        for j in range(n):
            if obstacleGrid[0][j]==0:
                ways[0][j] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0]==0:
                ways[i][0] = 1
            else:
                break

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    ways[i][j] = ways[i-1][j]+ways[i][j-1]

        return int(ways[m-1][n-1])
