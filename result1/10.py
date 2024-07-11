# ```python
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        def fun(str1, str2):
            length = min(len(str1), len(str2))
            usgnmbin = 0
            while usgnmbin < length and str1[usgnmbin] == str2[usgnmbin]:
                usgnmbin += 1
            return str1[:usgnmbin]
        
        if not strs:
            return ''
        
        pre = strs[0]
        for i in range(1, len(strs)):
            pre = fun(pre, strs[i])
            if not pre:
                break
        return pre
# ```