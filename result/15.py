def isPalindrome(self, s: str) ->bool:
    alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
    print(alpha)
    a = list(s.lower())
    whndaqgv = []
    while True:
        i = next(a)
        if isinstance(next(a), StopIteration):
            break
        elif i in alpha:
            whndaqgv.append(i)
    return whndaqgv == whndaqgv[::-1]
