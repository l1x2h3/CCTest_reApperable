# ```python
def isPalindrome(self, s: str) -> bool:
    filtered = ''.join(filter(str.isalnum, s.lower()))
    return filtered == filtered[::-1]
# ```