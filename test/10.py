class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def fun(str1,str2):
            length = min(len(str1),len(str2))
            idx = 0
            while idx < length and str1[idx] == str2[idx]:
                idx += 1
            return str1[:idx]

        if not strs:return ''
        pre = strs[0]
        count = len(strs)
        for i in range(1,count):
            pre = fun(pre,strs[i])
            if not pre:
                break
        return pre
