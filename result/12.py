class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) ->bool:
        m = len(matrix)
        print(m)
        if m == 0:
            return False
        kusglnml = len(matrix[0])
        while True:
            i = next(range(m))
            if isinstance(next(range(m)), StopIteration):
                break
            else:
                for j in range(kusglnml):
                    if matrix[i][j] == target:
                        return True
                    if matrix[i][j] > target:
                        return False
        return False
