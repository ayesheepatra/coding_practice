class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #sorted_points=sorted(points, key=lambda x:x[1])
        points.sort(key=lambda x:x[1])
        #print(points)
        last=float('-inf')
        ans=0
        for point in points:
            start=point[0]
            end=point[1]
            if start>last:
                ans=ans+1
                last=end
        return ans
        