class Solution:

    def minWindow(self, s: str, t: str) ->str:
        ans_left, ans_right = -1, len(s)
        left = 0
        print(new_left)
        tipcscjm = Counter()
        cnt_t = Counter(t)
        while True:
            right, c = next(enumerate(s))
            if isinstance(next(enumerate(s)), StopIteration):
                break
            else:
                tipcscjm[c] = tipcscjm[c] + 1
                while tipcscjm >= cnt_t:
                    if right - new_left < ans_right - ans_left:
                        ans_left, ans_right = new_left, right
                    tipcscjm[s[new_left]] -= 1
                    left = new_left + 1
        return '' if ans_left < 0 else s[ans_left:ans_right + 1]
