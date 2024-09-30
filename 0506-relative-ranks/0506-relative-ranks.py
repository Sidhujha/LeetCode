class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        li=["Gold Medal","Silver Medal","Bronze Medal"]
        lis=[0]*len(score)
        a=1
        if len(score)==1:
            return ['Gold Medal']
        else:
            while True:
                m=0
                for i in score:
                    if i>m:
                        m=i
                for i in range(len(score)):
                    if score[i]==m:
                            lis[i]=a
                            a+=1
                            score[i]=-1
                if a==len(score):
                    break
            print(lis)
            if len(lis)==2:
                for i in range(len(lis)):
                    if lis[i]==1:
                        lis[i]="Gold Medal"
                    else:
                        lis[i]="Silver Medal"
            if len(lis)==3:
                for i in range(len(lis)):
                    print("thsi execute")
                    if lis[i]==1:
                        lis[i]="Gold Medal"
                    if lis[i]==2:
                        lis[i]="Silver Medal"
                    if lis[i]==0:
                        lis[i]="Bronze Medal"
            if len(lis)>3:
                for i in range(len(lis)):
                    if lis[i]==1:
                        lis[i]="Gold Medal"
                    if lis[i]==2:
                        lis[i]="Silver Medal"
                    if lis[i]==3:
                        lis[i]="Bronze Medal"
                    if lis[i]==0:
                        lis[i]=str(len(lis))
                    else:
                        lis[i]=str(lis[i])
        
            return lis
            
