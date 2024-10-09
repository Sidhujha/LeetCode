class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        while "()" in s:
            s=s.replace("()","")
        print(s)
        return len(s)