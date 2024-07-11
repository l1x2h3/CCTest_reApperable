# ```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        maxlen = 0
        for end, char in enumerate(s):
            if char in hashmap and hashmap[char] >= start:
                start = hashmap[char] + 1
            hashmap[char] = end
            maxlen = max(maxlen, end - start + 1)
        return maxlen
# ```