class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        numA = 0
        dicts = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                numA += 1
            else:
                dicts[secret[i]] = dicts.get(secret[i],0) + 1
                dicts[guess[i]] = dicts.get(guess[i],0) - 1
        numb = len(secret) - numA
        for v in dicts.values():
            if v > 0:
                numb -= v
        return '{}A{}B'.format(numA,numb)
