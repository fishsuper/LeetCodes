# 搜索二维矩阵II

# 遍历，没用充分利用列的增序
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        #YorN = False
        for i in range(m):
            if target<=matrix[i][n-1] and target>=matrix[i][0]:
                for j in range(n):
                    if target==matrix[i][j]: return True
        return False
        
# 对每一行用二分法查找
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            right = n-1
            left = 0
            mid = (left+right)//2
            while target!=matrix[i][mid]:
                if target<matrix[i][mid]:
                    right = mid
                if target>matrix[i][mid]:
                    left = mid
                mid = (left+right)//2
                if right-left<=1:  # 注意这个条件是为了在此行中没有target的情况跳出循环
                    break
            if target==matrix[i][mid] or target==matrix[i][right]:  
                # 增加后面一种情况，因为mid可能取不到右端点，比如[-1,3]，target=3
                return True
        return False

