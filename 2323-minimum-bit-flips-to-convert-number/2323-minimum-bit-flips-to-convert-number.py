class Solution:
    def minBitFlips(self, s: int, g: int) -> int:
        s1=""
        s2=""
        while s>0:
            s1+=str(s%2)
            s//=2
        while g>0:
            s2+=str(g%2)
            g//=2
        c=0
        for i in range(min(len(s1),len(s2))):
            if s1[i]!=s2[i]:
                c+=1
        return c+abs(len(s1)-len(s2))