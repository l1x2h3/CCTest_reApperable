# ```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
                guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1
        
        for key in secret_count:
            if key in guess_count:
                cows += min(secret_count[key], guess_count[key])
        
        return f'{bulls}A{cows}B'
# ```