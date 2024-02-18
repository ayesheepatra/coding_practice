class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mapp=Counter(arr)
        freq_list=list(mapp.values())
        freq_list.sort()
        count=0
        for i in range(len(freq_list)):
            if freq_list[i]>k:
                freq_list[i]=freq_list[i]-k
                k=0
            else:
                k=k-freq_list[i]
                freq_list[i]=0
            if freq_list[i]!=0:
                count=count+1
        return count

        