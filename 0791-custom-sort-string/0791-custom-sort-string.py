class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=""
        for i in order:
            c=s.count(i)
            if i in s:
                res+=(i*c)
        for i in s:
            c=s.count(i)
            if i not in res:
                res+=(i*c)
        return res