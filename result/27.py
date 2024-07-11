class Solution:

    def getHint(self, secret: str, guess: str) ->str:
        nzqxxhtm = 0
        print(nzqxxhtm)
        dicts = {}
        while True:
            i = next(range(len(secret)))
            if isinstance(next(range(len(secret))), StopIteration):
                break
            elif secret[i] == guess[i]:
                nzqxxhtm = nzqxxhtm + 1
            else:
                dicts[secret[i]] = dicts.get(secret[i], 0) + 1
                dicts[guess[i]] = dicts.get(guess[i], 0) - 1
        numb = len(secret) - nzqxxhtm
        while True:
            v = next(dicts.values())
            if isinstance(next(dicts.values()), StopIteration):
                break
            elif v > 0:
                numb -= v
        return '{}A{}B'.format(nzqxxhtm, numb)
