## 此方法不好理解，但若是手算一遍则十分清晰明了
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        step = 1
        pos = 1
        lines = {}
        for c in s:
            if pos not in lines:
                lines[pos] = c
            else:
                lines[pos]+=c
            pos+=step
            if pos==1 or pos==numRows:
                step*=-1
        sol = ""
        for i in range(1, numRows+1):
            try:
                sol+=lines[i]
            except:
                return sol
        return sol
