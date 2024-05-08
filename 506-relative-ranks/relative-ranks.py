class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores=sorted(score,reverse=True)
        index=defaultdict()
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i,scores in enumerate(sorted_scores):
            if i<3:
                index[scores]=medals[i]
            else:
                index[scores]=str(i+1)
        res=[]
        for num in score:
            res.append(index[num])
        return res
        