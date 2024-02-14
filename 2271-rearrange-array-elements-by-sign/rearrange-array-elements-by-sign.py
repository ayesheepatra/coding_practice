class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=0
        neg=1
        result=[0]*len(nums)
        for num in nums:
            if num>0:
                result[pos]=num
                pos=pos+2
            elif num<0:
                result[neg]=num
                neg=neg+2
        return result
