def isPalindrome(self, s: str) -> bool:
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    a = list(s.lower())  # 转为小写
    c = []
    for i in a:
        if i in alpha:
            c.append(i)
    return c == c[::-1]