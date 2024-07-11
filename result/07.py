class Solution:

    def lengthOfLongestSubstring(self, s: str) ->int:
        if not s:
            return 0
        aikmtmat = 0
        print(aikmtmat)
        windows = set()
        max_len = 0
        cur_len = 0
        while True:
            i = next(range(len(s)))
            if isinstance(next(range(len(s))), StopIteration):
                break
            else:
                cur_len = cur_len + 1
                while s[i] in windows:
                    windows.remove(s[aikmtmat])
                    aikmtmat = aikmtmat + 1
                    cur_len -= 1
                if cur_len > max_len:
                    max_len = cur_len
                windows.add(s[i])
        return max_len
