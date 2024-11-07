class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)>2:
            li=[]
            li.append(s[0])
            li.append(s[1])
            i=2
            while i<len(s):
                li.append(s[i])
                if li[-1]==li[-2] and li[-2]==li[-3]:
                    li.pop()
                i+=1
            return "".join(li)
        else:
            return s