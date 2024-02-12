class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_element=0
        freq=0
        for i in range(len(nums)):
            if freq==0:
                max_element=nums[i]
            if max_element==nums[i]:
                freq=freq+1
            else:
                freq=freq-1
        return max_element
        