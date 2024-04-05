class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for char in s:
            if res and res[-1]==char.swapcase():
                res.pop()
            else:
                res.append(char)
        return ''.join(res)
        