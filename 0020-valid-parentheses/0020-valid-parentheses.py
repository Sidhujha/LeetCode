class Solution:
    def isValid(self, s: str) -> bool:
        while("()" in s or "{}" in s or "[]" in s):
            if "()" in s:
                s=s.replace("()","")
            if "{}" in s:
                s=s.replace("{}","")
            if "[]" in s:
                s=s.replace("[]","")
        if len(s)==0:
            return True