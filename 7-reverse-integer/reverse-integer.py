class Solution:
    def reverse(self, x: int) -> int:
        res=''
        flag=False
        if x<0:
            flag=True
            x=x*(-1)
        while x >=10:
            r=x%10
            res=res+str(r)
            x=x//10
        res=res+str(x)
        if int(res) > 2**31-1:
            return 0
        return (-1*int(res)) if flag==True else  int(res)
        