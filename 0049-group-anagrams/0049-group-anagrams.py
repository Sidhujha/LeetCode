class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st=[]
        for i in strs:
            i=sorted(i)
            st.append("".join(i))
        li=[]
        for i in range(len(strs)):
            lis=[]
            for j in range(i+1,len(strs)):
                if st[i]==st[j]:
                    lis.append(strs[j])
                    strs[j]="0"
            lis.append(strs[i])
            li.append(lis)
        for i in li[::-1]:
            if '0' in i:
                li.remove(i)
        li.sort()
        return li