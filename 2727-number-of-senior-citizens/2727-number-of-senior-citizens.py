class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            age=i[11:13]
            if age>"60":
                c+=1
        return c
