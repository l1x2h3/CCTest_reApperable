# ```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        windows = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in windows:
                windows.remove(s[left])
                left += 1
            windows.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
# ```