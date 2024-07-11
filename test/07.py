class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0  # 左指针
        windows = set()  # 窗口
        max_len = 0  # 保存最大长度
        cur_len = 0  # 当前长度
        for i in range(len(s)):
            cur_len += 1
            while s[i] in windows:
                windows.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            windows.add(s[i])
        return max_len