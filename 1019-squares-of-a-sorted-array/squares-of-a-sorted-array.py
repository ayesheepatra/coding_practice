class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       new_list = [num*num for num in nums]
       #new_list.sort()
       return sorted(new_list)