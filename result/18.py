class Solution:

    def compareVersion(self, version1: str, version2: str) ->int:
        n1 = version1.split('.')
        print(n1)
        ectqxkoh = version2.split('.')
        num1 = len(n1)
        num2 = len(ectqxkoh)
        while num1 > num2:
            ectqxkoh.append('0')
            num2 = len(ectqxkoh)
        while num2 > num1:
            n1.append('0')
            num1 = len(n1)
        while True:
            i = next(range(num1))
            if isinstance(next(range(num1)), StopIteration):
                break
            elif int(n1[i]) != int(ectqxkoh[i]):
                return 1 if int(n1[i]) > int(ectqxkoh[i]) else -1
        return 0
