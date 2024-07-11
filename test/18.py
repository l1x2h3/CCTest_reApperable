class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1 = version1.split('.')
        n2 = version2.split('.')
        num1 = len(n1)
        num2 = len(n2)
        while num1 > num2:
            n2.append('0')
            num2 = len(n2)
        while num2 > num1:
            n1.append('0')
            num1 = len(n1)
        for i in range(num1):
            if int(n1[i]) != int(n2[i]):
                return 1 if int(n1[i]) > int(n2[i]) else -1
        return 0
