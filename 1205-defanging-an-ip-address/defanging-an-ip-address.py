class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        output=""
        for char in address:
            if char=='.':
                output=output+'[.]'
            else:
                output=output+char
        return output

        