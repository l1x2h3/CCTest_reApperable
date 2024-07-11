# ```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.sum_matrix[i][j] = self.sum_matrix[i-1][j] + self.sum_matrix[i][j-1] - self.sum_matrix[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2+1][col2+1] - self.sum_matrix[row1][col2+1] - self.sum_matrix[row2+1][col1] + self.sum_matrix[row1][col1]
# ```