# ```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        strs.sort()
        first, last = strs[0], strs[-1]
        idx = 0
        while idx < len(first) and idx < len(last) and first[idx] == last[idx]:
            idx += 1
        return first[:idx]
# ```