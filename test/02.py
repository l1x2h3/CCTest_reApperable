# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        hashmap = {}
        start, end = 0,0
        maxlen = 0
        for i,j in enumerate(s):
            if j in hashmap:
                if start>hashmap[j]:
                    hashmap[j] = i
                else:
                    start = hashmap[j] + 1
            end += 1
            hashmap[j] = i
            maxlen = max([maxlen, end-start])
        return maxlen