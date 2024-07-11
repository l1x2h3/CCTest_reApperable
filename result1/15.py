# ```python
def isPalindrome(self, s: str) -> bool:
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    filtered_chars = [c for c in s.lower() if c in alpha]
    return filtered_chars == filtered_chars[::-1]
# ```