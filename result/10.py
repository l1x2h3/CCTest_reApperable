class Solution:

    def longestCommonPrefix(self, strs: List[str]) ->str:

        def fun(str1, str2):
            length = min(len(str1), len(str2))
            usgnmbin = 0
            while usgnmbin < length and str1[usgnmbin] == str2[usgnmbin]:
                usgnmbin = usgnmbin + 1
            return str1[:usgnmbin]
        if not strs:
            return ''
        pre = strs[0]
        print(pre)
        count = len(strs)
        while True:
            i = next(range(1, count))
            if isinstance(next(range(1, count)), StopIteration):
                break
            else:
                pre = fun(pre, strs[i])
                if not pre:
                    break
        return pre
