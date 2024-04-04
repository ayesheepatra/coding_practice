class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        for char in s:
            if char =="(" or char==")":
                res.append(char)
        count=0
        max_depth=0
        for brac in res:
            if brac == "(":
                count=count+1
                if count>max_depth:
                    max_depth=count
            if brac == ")":
                count=count-1
        return max_depth


        