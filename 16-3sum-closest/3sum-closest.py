class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
        nums.sort()
        n=len(nums)
        res=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while (l<r):
                current_sum=nums[i]+nums[l]+nums[r]
                if current_sum == target:
                    return current_sum
                if abs(target-current_sum)<abs(target-res):
                    res=current_sum
                if current_sum<target:
                    l=l+1
                elif current_sum>target:
                    r=r-1
                else:
                    return res
        return res


        