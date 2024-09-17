class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_list=[]
        
        for time in timePoints:
            h,m = map(int, time.split(":"))
            minute= h*60 + m
            min_list.append(minute)
        min_list.sort()
        #print(min_list)
        res = 60 * 24 - min_list[-1] + min_list[0]
        for i in range(len(min_list)-1):
            curr = min_list[i+1]
            prev = min_list[i]
            diff = curr - prev
            res = min(res, diff)
        return res




        