class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        s_list = []
        a = 1
        for i in s:
            if i in dct:
                s_list.append(dct[i])
            else:
                s_list.append(a)
                dct[i] = a
                a += 1

        dct = {}
        t_list = []
        b = 1
        for i in t:
            if i in dct:
                t_list.append(dct[i])
            else:
                t_list.append(b)
                dct[i] = b
                b += 1
        return t_list == s_list
