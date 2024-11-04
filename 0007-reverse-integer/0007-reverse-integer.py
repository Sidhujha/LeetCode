class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        mi=-2147483648
        ma=2147483647
        li=[]
        for i in range(len(str(x))):
            if str(x)[i]>'0':
                li.append(i)
                break
        for i in range(len(str(x))-1,-1,-1):
            if str(x)[i]>'0':
                li.append(i)
                break
        n=str(x)
        if x==0:
            return 0
        if x>0:
            a=li[0]
            b=li[1]+1
            c=n[a:b]
            c=c[::-1]
            if int(c)<ma:
                return int(c)
            else:
                return 0
        if x<0:
            a=li[0]
            b=li[1]+1
            d="-"
            c=n[a:b]
            c=c[::-1]
            d=d+c
            if int(d)>mi:
                return int(d)
            else:
                return 0
        