class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2,p3,p5=0,0,0
        li=[1]
        i=1
        while(i<n):
            a=min(li[p2]*2,li[p3]*3,li[p5]*5)
            if a==li[p2]*2:
                p2+=1
            elif a==li[p3]*3:
                p3+=1
            elif a==li[p5]*5:
                p5+=1
            if li[i-1]==a:
                continue
            else:
                li.append(a)
                i+=1
        return li[-1]
            