# ```python
class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(s):
            dct = {}
            return [dct.setdefault(c, len(dct)) for c in s]
        
        return transform(s) == transform(t)
# ```