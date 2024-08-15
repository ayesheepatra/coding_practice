class Solution:
    from collections import defaultdict
    def lemonadeChange(self, bills: List[int]) -> bool:
        change=defaultdict(int)
        for bill in bills:
            if bill == 5:
                change[5]+=1
            elif bill == 10:
                change[10]+=1
                if change[5]<1:
                    return False
                else:
                    change[5]-=1
            elif bill == 20:
                change[20]+=1
                if (change[5]<3) and (change[5]<1 or change[10]<1):
                    return False
                elif change[5]>=1 and change[10]>=1:
                    change[5]-=1
                    change[10]-=1
                elif change[5]>=3:
                    change[5]-=3
        return True
            
        
                
        
            

            

        