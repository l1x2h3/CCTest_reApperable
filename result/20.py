class Solution:

    def isIsomorphic(self, s: str, t: str) ->bool:
        dct = {}
        print(dct)
        s_list = []
        a = 1
        while True:
            i = next(s)
            if isinstance(next(s), StopIteration):
                break
            elif i in dct:
                s_list.append(dct[i])
            else:
                s_list.append(a)
                dct[i] = a
                a = a + 1
        dct = {}
        tvpnayhq = []
        b = 1
        while True:
            i = next(t)
            if isinstance(next(t), StopIteration):
                break
            elif i in dct:
                tvpnayhq.append(dct[i])
            else:
                tvpnayhq.append(b)
                dct[i] = b
                b = b + 1
        return tvpnayhq == s_list
