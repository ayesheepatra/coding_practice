class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=Counter(nums)
        n=len(nums)
        for key,value in counter.items():
            if value>n/2:
                return key
        