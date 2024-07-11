class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    return False
        return False

