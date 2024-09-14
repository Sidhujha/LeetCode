class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pa=[prices[0]]
        sa=[prices[-1]]
        for i in prices[1:]:
            mi=min(i,pa[-1])
            pa.append(mi)
        for i in prices[-2::-1]:
            ma=max(i,sa[-1])
            sa.append(ma)
        sa=sa[::-1]
        maxs=0
        for i in range(len(pa)):
            if abs(pa[i]-sa[i])>maxs:
                maxs=abs(pa[i]-sa[i]) 
        
        return maxs