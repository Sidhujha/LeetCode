class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c=-1
        if needle in haystack:
            c=haystack.index(needle)
        return c