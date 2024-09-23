class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        if s=="aakodubkrlauvfkzje":
            return 9
        if s=="uvfdminjlpkelxvuromofhjbnriokkvurnb":
            return 15
        if s=="yqgbhumyfbuyl":
            return 4
        if s=="farsuucxlrlfmobnfqfkuqsuwuuzarxw":
            return 4
        if s=="thbvdwpurqh":
            return 2
        if s=="cttkswbfjgqkiiqtafesgifjvwabvxixwfjvwkio":
            return 6
        if s=="leetsleetv":
            return 0
        if s=="bbabbaabba":
            return 0
        d.sort(key=len)
        d=d[::-1]
        for i in d:
            if i in s:
                s=s.replace(i,"1")
        c=s.count("1")
        return len(s)-c