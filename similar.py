import pycode_similar

# 示例代码片段
code1 = """
def add(a, b):
    return a + b
"""

code2 = """
def add(x, y):
    return x + y
"""

code3 = """
def multiply(a, b):
    return a * b
"""

# 计算代码相似度
report, overall_similarity = pycode_similar.detect([code1, code2, code3], diff_method=pycode_similar.UnifiedDiff)
print(report)
# 打印结果
for index, (similarity, src, other_src) in enumerate(report):
    print(f"Pair {index + 1}:")
    print(f"  Similarity: {similarity * 100:.2f}%")
    print(f"  Source 1: {src}")
    print(f"  Source 2: {other_src}")
    print()

print(f"Overall similarity: {overall_similarity * 100:.2f}%")