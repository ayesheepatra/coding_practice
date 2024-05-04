class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i=0
        j=len(people)-1
        boats=0
        while(i<=j):
            if people[i]+people[j]<=limit:
                boats+=1
                i=i+1
                j=j-1
            else:
                boats+=1
                j-=1
        return boats
        