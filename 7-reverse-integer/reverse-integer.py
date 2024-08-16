class Solution:
    def reverse(self, x: int) -> int:
        res=0
        flag = False
        if x < 0:
            flag = True
            x = x * -1
        while x > 0:
            r = x % 10
            res = (res * 10) + r
            x = x // 10
        if res > (2 ** 31) - 1 or res < (-2 ** 31):
            return 0
        return res if flag == False else res * -1
        