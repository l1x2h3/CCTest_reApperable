# 给定一个
# n × n
# 的二维矩阵
# matrix
# 表示一个图像。请你将图像顺时针旋转
# 90
# 度。
#
# 你必须在
# 原地
# 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要
# 使用另一个矩阵来旋转图像。
#

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 不能写成 matrix = matrix_new
        matrix[:] = matrix_new

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/rotate-image/solutions/526980/xuan-zhuan-tu-xiang-by-leetcode-solution-vu3m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。