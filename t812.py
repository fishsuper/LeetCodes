# 812题： 给你一个由 X-Y 平面上的点组成的数组 points ，其中 points[i] = [xi, yi] 。
# 从其中取任意三个不同的点组成三角形，返回能组成的最大三角形的面积。与真实值误差在 10-5 内的答案将会视为正确答案。

# 使用Numpy包的向量叉积运算
def largestTriangleArea(points: list[list[int]]) -> float:
        import numpy as np 
        n = len(points)
        Area = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    a = np.array(points[i])-np.array(points[j])
                    b = np.array(points[i])-np.array(points[k])
                    a_b = np.cross(a,b)
                    Area = max(np.linalg.norm(a_b)/2.0, Area)
        return Area

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]

print(largestTriangleArea(points))

# 点到直线的距离公式
def largestTriangleArea1(points: list[list[int]]) -> float:
        n = len(points)
        Area = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    A = points[i][1]-points[j][1]
                    B = -(points[i][0]-points[j][0])
                    C = -B*points[i][1]-A*points[i][0]
                    d = abs(A*points[k][0]+B*points[k][1]+C)/2
                    Area = max(d, Area)
        return Area

# 用行列式
from itertools import combinations
def largestTriangleArea2(points: list[list[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2
        return max(triangleArea(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3))

print(largestTriangleArea2(points))

## 官方解答
# 以上都是枚举法，时间复杂度O(n**3)
# 先使用 Andrew 算法求出所有点对应的凸包，因为面积最大的三角形顶点一定在凸包上
# 在凸包上枚举三角形

class Solution:
    def getConvexHull(self, points: list[list[int]]) -> list[list[int]]:
        def cross(p: list[int], q: list[int], r: list[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(points)
        if n < 4:
            return points

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        points.sort()

        hull = []
        # 求凸包的下半部分
        for i, p in enumerate(points):
            while len(hull) > 1 and cross(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            while len(hull) > m and cross(hull[-2], hull[-1], points[i]) <= 0:
                hull.pop()
            hull.append(points[i])
        hull.pop()  # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        return hull

    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def triangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> float:
            return abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2) / 2

        convexHull = self.getConvexHull(points)
        ans, n = 0, len(convexHull)
        for i, p in enumerate(convexHull):
            k = i + 2
            for j in range(i + 1, n - 1):
                q = convexHull[j]
                while k + 1 < n:
                    curArea = triangleArea(p[0], p[1], q[0], q[1], convexHull[k][0],convexHull[k][1])
                    nextArea = triangleArea(p[0], p[1], q[0], q[1], convexHull[k + 1][0], convexHull[k + 1][1])
                    if curArea >= nextArea:
                        break
                    k += 1
                ans = max(ans, triangleArea(p[0], p[1], q[0], q[1], convexHull[k][0], convexHull[k][1]))
        return ans



