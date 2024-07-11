# ```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = list(map(int, version1.split('.')))
        n2 = list(map(int, version2.split('.')))
        max_len = max(len(n1), len(n2))
        n1 += [0] * (max_len - len(n1))
        n2 += [0] * (max_len - len(n2))
        for v1, v2 in zip(n1, n2):
            if v1 != v2:
                return 1 if v1 > v2 else -1
        return 0
# ```