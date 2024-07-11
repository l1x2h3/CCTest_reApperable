# ```python
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        matrix[:] = [list(row) for row in zip(*matrix[::-1])]
# ```