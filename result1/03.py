# ```python
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, len(s)
        left = 0
        tipcscjm = Counter()
        cnt_t = Counter(t)
        for right, c in enumerate(s):
            tipcscjm[c] += 1
            while tipcscjm >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                tipcscjm[s[left]] -= 1
                left += 1
        return '' if ans_left < 0 else s[ans_left:ans_right + 1]
# ```