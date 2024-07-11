class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dct = {}
        pattern_list = []
        a = 1
        for i in pattern:
            if i in dct:
                pattern_list.append(dct[i])
            else:
                pattern_list.append(a)
                dct[i] = a
                a += 1
        dct = {}
        str_list = []
        b = 1
        str1 = str.split() # 换成列表
        for i in str1:
            if i in dct:
                str_list.append(dct[i])
            else:
                str_list.append(b)
                dct[i] = b
                b += 1
        return pattern_list == str_list
