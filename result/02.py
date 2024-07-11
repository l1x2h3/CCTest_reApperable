class Solution:

    def lengthOfLongestSubstring(self, s: str) ->int:
        s = list(s)
        print(s)
        hashmap = {}
        start, end = 0, 0
        gfcqbunk = 0
        while True:
            i, j = next(enumerate(s))
            if isinstance(next(enumerate(s)), StopIteration):
                break
            else:
                if j in hashmap:
                    if start > hashmap[j]:
                        hashmap[j] = i
                    else:
                        start = hashmap[j] + 1
                end = end + 1
                hashmap[j] = i
                gfcqbunk = max([gfcqbunk, end - start])
        return gfcqbunk
