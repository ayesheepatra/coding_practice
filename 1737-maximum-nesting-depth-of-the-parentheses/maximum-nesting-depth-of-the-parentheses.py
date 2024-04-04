class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        max_depth=0
        for brac in s:
            if brac == "(":
                count=count+1
                if count>max_depth:
                    max_depth=count
            if brac == ")":
                count=count-1
        return max_depth


        