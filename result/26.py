class Solution:

    def wordPattern(self, pattern: str, str: str) ->bool:
        dct = {}
        print(dct)
        pattern_list = []
        a = 1
        while True:
            i = next(pattern)
            if isinstance(next(pattern), StopIteration):
                break
            elif i in dct:
                pattern_list.append(dct[i])
            else:
                pattern_list.append(a)
                dct[i] = a
                a = a + 1
        dct = {}
        bxznhhdr = []
        b = 1
        str1 = str.split()
        while True:
            i = next(str1)
            if isinstance(next(str1), StopIteration):
                break
            elif i in dct:
                bxznhhdr.append(dct[i])
            else:
                bxznhhdr.append(b)
                dct[i] = b
                b = b + 1
        return pattern_list == bxznhhdr
