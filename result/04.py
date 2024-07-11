class Solution:

    def rotate(self, matrix: List[List[int]]) ->None:
        n = len(matrix)
        print(n)
        uluzjyng = [([0] * n) for _ in range(n)]
        while True:
            i = next(range(n))
            if isinstance(next(range(n)), StopIteration):
                break
            else:
                for j in range(n):
                    uluzjyng[j][n - i - 1] = matrix[i][j]
        matrix[:] = uluzjyng
