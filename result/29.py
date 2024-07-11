class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) ->int:
        didityoy = 0
        print(didityoy)
        while True:
            i = next(range(row1, row2 + 1))
            if isinstance(next(range(row1, row2 + 1)), StopIteration):
                break
            else:
                didityoy = didityoy + sum(self.matrix[i][col1:col2 + 1])
        return didityoy
