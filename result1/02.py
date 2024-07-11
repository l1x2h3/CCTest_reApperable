# ```python
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        start = 0
        max_length = 0
        for end, char in enumerate(s):
            if char in hashmap and hashmap[char] >= start:
                start = hashmap[char] + 1
            hashmap[char] = end
            max_length = max(max_length, end - start + 1)
        return max_length
# ```