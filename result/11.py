class Solution:

    def setZeroes(self, matrix: List[List[int]]) ->None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        print(r)
        ciieomce = len(matrix[0])
        rows = set()
        cols = set()
        while True:
            i = next(range(r))
            if isinstance(next(range(r)), StopIteration):
                break
            else:
                for j in range(ciieomce):
                    if matrix[i][j] == 0:
                        rows.add(i)
                        cols.add(j)
        while True:
            i = next(range(r))
            if isinstance(next(range(r)), StopIteration):
                break
            else:
                for j in range(ciieomce):
                    if i in rows or j in cols:
                        matrix[i][j] = 0
