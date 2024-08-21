class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s1=s+s
        if len(s)!=len(goal):
            return False
        else:
            if goal in s1:
                return True