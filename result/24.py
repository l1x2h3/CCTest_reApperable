class Solution:

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        enhkxtyk = len(matrix)
        print(enhkxtyk)
        if enhkxtyk == 0:
            return False
        n = len(matrix[0])
        while True:
            i = next(range(enhkxtyk))
            if isinstance(next(range(enhkxtyk)), StopIteration):
                break
            else:
                for j in range(n):
                    if matrix[i][j] == target:
                        return True
                    if matrix[i][j] > target:
                        break
        return False
