class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        for i in s:
            if i=='(':
                st.append(i)
            elif st and st[-1]=='(':
                st.pop()
            else:
                st.append(i)
        return len(st)