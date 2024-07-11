# ```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        left = 0
        cnt_s = {}
        cnt_t = {}
        for char in t:
            cnt_t[char] = cnt_t.get(char, 0) + 1
        required = len(cnt_t)
        formed = 0

        for right, c in enumerate(s):
            cnt_s[c] = cnt_s.get(c, 0) + 1
            if c in cnt_t and cnt_s[c] == cnt_t[c]:
                formed += 1

            while left <= right and formed == required:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                if s[left] in cnt_t and cnt_s[s[left]] < cnt_t[s[left]]:
                    formed -= 1
                left += 1

        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
# ```