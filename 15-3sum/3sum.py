class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        nums.sort()
        for i in range(n-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while (l<r):
                summation=nums[i]+nums[l]+nums[r]
                if summation>0:
                    r=r-1
                elif summation<0:
                    l=l+1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

        