class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        li=[]
        for i in range(1,n+1):
            li.append(str(i))
        li.sort()
        li=[int(i) for i in li]
        return li