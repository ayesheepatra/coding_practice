class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i=j=0
        while i<len(version1) or j<len(version2):
            num1=0
            num2=0
            while i<len(version1) and version1[i]!='.':
                num1=num1*10+int(version1[i])
                i=i+1
            while j<len(version2) and version2[j]!='.':
                num2=num2*10+int(version2[j])
                j=j+1
            if num1<num2:
                return -1
            elif num1>num2:
                return 1
            i=i+1
            j=j+1
        return 0
        
        