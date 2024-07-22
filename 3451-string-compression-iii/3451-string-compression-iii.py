class Solution:
    def compressedString(self, s: str) -> str:
        res=""
        c=0
        li=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                c+=1
            else:
                li.append((c+1))
                c=0
        li.append((c+1))
        li1=[]
        su=0
        for i in li:
            li1.append(su)
            su+=int(i)
        for i in range(len(li1)):
            if (li[i])>9:
                while((li[i])>0):
                    if li[i]>9:
                        res=res+'9'+s[li1[i]]
                        li[i]-=9
                    else:
                        res=res+str(li[i])+s[li1[i]]
                        li[i]=0
            else:
                res=res+str(li[i])+s[li1[i]]
        return res