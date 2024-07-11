# ```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        def encode(s):
            dct = {}
            encoded = []
            code = 1
            for i in s:
                if i not in dct:
                    dct[i] = code
                    code += 1
                encoded.append(dct[i])
            return encoded
        
        pattern_list = encode(pattern)
        str_list = encode(str.split())
        
        return pattern_list == str_list
# ```