class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_map={}
        for i in range(len(nums)):
            if target-nums[i] in index_map:
                return [index_map[target-nums[i]],i]
            else:
                index_map[nums[i]]=i
        return []
                
        