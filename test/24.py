class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] > target:
                    break
        return False
